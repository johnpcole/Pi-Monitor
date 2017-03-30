//Sets up the refresh when the page loads

$(document).ready(function ()
{
    //updateBuildTiles();
    // Refresh the tiles every minute.
    setInterval(function()
    {
        //alert("hi")
        updateTorrent('Refresh');
    }, 10000);
});



// Ajax call for all torrent data

function updateTorrent(action)
{
    var pathname = window.location.pathname;
    $.getJSON('UpdateTorrent='+action+'-'+pathname.substring(9))
        .done(function (data)
        {
            updateTorrentTile(torrentdata);
        });
};



// Update the displayed data

function updateTorrentTile(dataitem)
{
    updateTorrentImage("Status", dataitem.status, "tilesubicon");
    updateTorrentData("Progress", dataitem.progress);
    updateTorrentData("SizeEta", "of "+dataitem.sizeeta);
};


// Update the displayed data value

function updateTorrentData(fieldname, fieldvalue)
{
    var tileData = document.getElementById(fieldname);
    if (tileData != null) {
        tileData.innerHTML = fieldvalue;
    } else {
        alert("updateTorrentData: "+fieldname);
    };
};


// Update the displayed image

function updateTorrentImage(fieldname, fieldimage, fieldclass)
{
    var tileData = document.getElementById(fieldname);
    if (tileData != null) {
        tileData.innerHTML = "<img class=\""+ fieldclass +"\" src=\"/static/images/" + fieldimage + ".png\" alt=\"" + fieldimage + "\" />";
    } else {
        alert("updateTorrentImage: "+ fieldname);
    }
};


// Show and hide text fields

function updateTextFields(displaymode)
{
    var fieldData = document.getElementById('textfields');
    if (fieldData != null) {
        if (displaymode == 'Show') {
            fieldData.innerHTML = "<input type=\"text\" name=\"moviename\" /><input type=\"text\" name=\"movieyear\" />";
        } else {
            fieldData.innerHTML = "";
        };
    } else {
        alert("Cant find text fields");
    }
};


