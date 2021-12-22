{
  "targets": [
    {
      "target_name": "node-gyp-electron",
      "cflags!": [
        "-fno-exceptions"
      ],
      "cflags_cc!": [
        "-fno-exceptions"
      ],
      "msvs_settings": {
        "VCCLCompilerTool": {
          "ExceptionHandling": 1
        }
      },
      "xcode_settings": {
        "OTHER_CFLAGS": [
          "-std=c++20"
        ]
      },
      "defines": [
        "NAPI_VERSION=8",
        "UNICODE",
        "_UNICODE"
      ],
      "sources": [
        "src/index.cpp"
      ],
      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")"
      ],
      "dependencies": [
        "<!(node -p \"require('node-addon-api').gyp\")"
      ]
    }
  ]
}
