{
  "targets": [
    {
      "target_name": "keymapping",
      "sources": [
        "src/string_conversion.cc",
        "src/keymapping.cc"
      ],
      "cflags!": ["-fno-exceptions"],
      "cflags_cc!": ["-fno-exceptions"],
      "cflags": ["-std=c++20"],
      "cflags_cc": ["-std=c++20"],
      "xcode_settings": {
        "OTHER_CPLUSPLUSFLAGS": ["-std=c++20"],
        "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
        "CLANG_CXX_LANGUAGE_STANDARD": "c++20"
      },
      "msvs_settings": {
        "VCCLCompilerTool": {
          "ExceptionHandling": 1,
          "AdditionalOptions": [
            "/std:c++20",
            "/W3"
          ]
        },
        "VCLinkerTool": {
          "AdditionalOptions": [
            "/guard:cf"
          ]
        }
      },
      "msvs_configuration_attributes": {
        "SpectreMitigation": "Spectre"
      },
      "defines": ["NAPI_DISABLE_CPP_EXCEPTIONS"],
      "conditions": [
        ["OS=='linux'", {
          "sources": [
            "deps/chromium/x/keysym_to_unicode.cc",
            "src/keyboard_x.cc"
          ],
          "include_dirs": [
            "<!@(${PKG_CONFIG:-pkg-config} x11 xkbfile --cflags | sed s/-I//g)"
          ],
          "libraries": [
            "<!@(${PKG_CONFIG:-pkg-config} x11 xkbfile --libs)"
          ],
          "cflags": ["-std=c++20"],
          "cflags_cc": ["-std=c++20"]
        }],
        ["OS=='freebsd'", {
          "sources": [
            "deps/chromium/x/keysym_to_unicode.cc",
            "src/keyboard_x.cc"
          ],
          "include_dirs": [
            "/usr/local/include"
          ],
          "link_settings": {
            "libraries": [
              "-lX11",
              "-lxkbfile",
              "-L/usr/local/lib"
            ]
          },
          "cflags": ["-std=c++20"],
          "cflags_cc": ["-std=c++20"]
        }],
        ["OS=='win'", {
          "sources": [
            "src/keyboard_win.cc"
          ]
        }],
        ["OS=='mac'", {
          "sources": [
            "src/keyboard_mac.mm"
          ],
          "link_settings": {
            "libraries": [
              "-framework Cocoa"
            ]
          }
        }],
        ["OS=='aix'", {
          "sources": [
            "deps/chromium/x/keysym_to_unicode.cc",
            "src/keyboard_x.cc"
          ],
          "link_settings": {
            "libraries": [
              "-lX11",
              "-lxkbfile"
            ]
          },
          "cflags": ["-std=c++20"],
          "cflags_cc": ["-std=c++20"]
        }]
      ]
    }
  ]
}
