#include <napi.h>
#include "filesystem.h"

Napi::Value Exists(const Napi::CallbackInfo& info)
{
    Napi::Env env = info.Env();

    if (info.Length() < 0 || !info[0].IsString())
    {
        Napi::TypeError::New(env, "Expected a string.").ThrowAsJavaScriptException();

        return env.Null();
    }

    std::string path = info[0].As<Napi::String>();

    bool result = FileSystem::exists(path);

    return Napi::Boolean::New(env, result);
}

Napi::Object Initialize(Napi::Env env, Napi::Object exports)
{
    exports.Set(
        "exists",
        Napi::Function::New(env, Exists)
    );

    return exports;
}

NODE_API_MODULE(natfs, Initialize);