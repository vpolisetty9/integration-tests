capabilities = """{

"target_capabilities" :{

    "desktop_firefox" :{
    "platform": "OS X 10.12",
    "screenResolution": "1600x1200",
    "browserName": "firefox",
    "version": "61.0",
    "tunnelIdentifier":"TUNNEL_IDENTIFIER"
    },

    "desktop_chrome" :{
      "platform": "OS X 10.12",
      "screenResolution": "1600x1200",
      "browserName": "chrome",
      "version": "68.0",
      "chromeOptions": {
        "args": ["start-maximized"]
      },
      "tunnelIdentifier":"TUNNEL_IDENTIFIER"
    },

    "desktop_chrome_headless" :{
      "platform": "Linux",
      "screenResolution": "1600x1200",
      "browserName": "chrome",
      "version": "68.0",
      "chromeOptions": {
        "args": ["headless"]
      },
      "tunnelIdentifier":"TUNNEL_IDENTIFIER"
    },

    "desktop_safari" :{
      "platform": "OS X 10.12.3",
      "screenResolution": "1600x1200",
      "browserName": "safari",
      "version": "11.0",
      "tunnelIdentifier":"TUNNEL_IDENTIFIER"
    },

    "desktop_ie" :{
      "platform": "Windows 10",
      "screenResolution": "1280x1024",
      "browserName": "internet explorer",
      "version": "11.0",
      "tunnelIdentifier":"TUNNEL_IDENTIFIER"
    }
 }

}"""
