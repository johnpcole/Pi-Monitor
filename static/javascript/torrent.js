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
    $.getJSON('UpdateTorrent='+pathname.substring(9)+'='+action)
        .done(function (data)
        {
            updateTorrentTile(data.selectedtorrent);
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
    var fieldArea = document.getElementById('textfields');
    if (fieldArea != null) {
        if (displaymode == 'Show') {
            var itemdetails = document.getElementById('Sanitisedname').innerHTML;
            var itemsplit = itemdetails.split("   (");
            var moviename = itemsplit[0]
            var itemsplit = itemsplit[1].split(")")
            var movieyear = itemsplit[0]
            fieldArea.innerHTML = "<input type=\"text\" name=\"moviename\" value=\""+moviename+"\"/><input type=\"text\" name=\"movieyear\" value=\""+movieyear+"\" />";
        } else {
            var moviename = document.getElementsByName('moviename')[0].value;
            var movieyear = document.getElementsByName('movieyear')[0].value;
            updateTorrent('Edit|'+moviename+"|"+movieyear);
            fieldArea.innerHTML = "";
        };
    } else {
        alert("Cant find text fields");
    }
};


