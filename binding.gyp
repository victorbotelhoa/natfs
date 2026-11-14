{
    "targets": [
        {
            "target_name": "natfs",

            "sources": [
                "src/addon.cpp",
                "depends/filesystem/src/filesystem.cpp",
                "depends/filesystem/src/fsobj.cpp"
            ],

            "include_dirs": [
                "<!@(node -p \"require('node-addon-api').include\")",
                "depends/filesystem/include"
            ],

            "dependencies": [
                "<!(node -p \"require('node-addon-api').gyp\")"
            ],

            "cflags!": ["-fno-exceptions"],
            "cflags_cc!": ["-fno-exceptions"],

            "defines": ["NAPI_CPP_EXCEPTIONS"],

            "msvs_settings": {
                "VCCLCompilerTool": {
                    "ExceptionHandling": 1
                }
            }
        }
    ]
}