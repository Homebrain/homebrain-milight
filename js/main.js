var WifiBoxModule = require('./wifibox.js');
var cmd = require('./commands.js');

var box = new WifiBoxModule("192.168.1.255", "8899");

// My zones
const ALL_ZONES = 0;
const OFFICE_LIGHT_STRIP = 3;
const OFFICE_CEIL = 4;

// Hues, should be in the range 0-255
const RED = 170;
const BLUE = 240;

function allOn() {
    for(var zone=1; zone<=4; zone++) {
        box.command(cmd.rgbw.on(zone));
        box.command(cmd.rgbw.whiteMode());
    }
};

function rotateHue(zone) {
    box.command(cmd.rgbw.on(zone));
    for(var hue=0; hue<360; hue++) {
        box.command(cmd.rgbw.hue(hue));
    }
};

// This is needed due to silly async issues
function repeat(f) {
    for(var i=0; i<15; i++) {
        f()
    }
}

function morning() {
    repeat(function() {
        box.command(cmd.rgbw.on(OFFICE_CEIL));
        box.command(cmd.rgbw.brightness(100));
        box.command(cmd.rgbw.whiteMode());
    });

    repeat(function() {
        box.command(cmd.rgbw.on(OFFICE_LIGHT_STRIP));
        box.command(cmd.rgbw.brightness(100));
        box.command(cmd.rgbw.hue(BLUE));
    });
};

function evening() {
    repeat(function() {
        box.command(cmd.rgbw.on(OFFICE_CEIL));
        box.command(cmd.rgbw.brightness(1));
        box.command(cmd.rgbw.hue(RED));
    });

    repeat(function() {
        box.command(cmd.rgbw.on(OFFICE_LIGHT_STRIP));
        box.command(cmd.rgbw.brightness(1));
        box.command(cmd.rgbw.hue(RED));
    });
}

repeat(function() {
    box.command(cmd.rgbw.off(1));
    box.command(cmd.rgbw.off(2));
});

//*
morning();
setTimeout(function() {
    evening();
}, 4000);
//box.command(cmd.white.allOn());
//*/
