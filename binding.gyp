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
      "cflags": ["-std=c++20", "-Wall", "-Wextra", "-Werror"],
      "cflags_cc": ["-std=c++20", "-Wall", "-Wextra", "-Werror"],
      "xcode_settings": {
        "OTHER_CPLUSPLUSFLAGS": ["-std=c++20", "-Wall", "-Wextra", "-Werror"],
        "GCC_ENABLE_CPP_EXCEPTIONS": "YES"
      },
      "msvs_settings": {
        "VCCLCompilerTool": {
          "ExceptionHandling": 1,
          "AdditionalOptions": [
            "/std:c++20",
            "/W4",
            "/WX",
            "/guard:cf",
            "/w34244",
            "/we4267",
            "/ZH:SHA_256"
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
          ]
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
          }
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
          }
        }]
      ]
    }
  ]
}
