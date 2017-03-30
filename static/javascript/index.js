//Sets up the refresh when the page loads

$(document).ready(function ()
{
    //updateBuildTiles();
    // Refresh the tiles every minute.
    setInterval(function()
    {
        //alert("hi")
        updateTorrentsInfo();
    }, 10000);
});



// Ajax call for all torrent data

function updateTorrentsInfo()
{
    $.getJSON('UpdateTorrentList')
        .done(function (data)
        {
            var torrentlist = data.torrents;
            $.each(torrentlist, function(index) {
                updateTorrentTile(torrentlist[index]);
            });
        });
};



// Update the displayed data

function updateTorrentTile(dataitem)
{
    tid = dataitem.torrentid
    var tile = document.getElementById("Torrent-"+tid);
    if (tile != null) {
        //tile.style.backgroundColor = "red";
        updateTorrentImage(tid, "Status", dataitem.status, "tilesubicon");
        updateTorrentData(tid, "Progress", dataitem.progress)
        updateTorrentData(tid, "SizeEta", "of "+dataitem.sizeeta)
    } else {
        alert("updateTorrentTile: "+dataitem.torrentid);
    }
};


// Update the displayed data value

function updateTorrentData(tid, fieldname, fieldvalue)
{
    var tileData = document.getElementById(fieldname+"-"+tid);
    if (tileData != null) {
        tileData.innerHTML = fieldvalue;
    } else {
        alert("updateTorrentData: "+fieldname+"-"+tid);
    }
};


// Update the displayed image

function updateTorrentImage(tid, fieldname, fieldimage, fieldclass)
{
    var tileData = document.getElementById(fieldname+"-"+tid);
    if (tileData != null) {
        tileData.innerHTML = "<img class=\""+ fieldclass +"\" src=\"/static/images/" + fieldimage + ".png\" alt=\"" + fieldimage + "\" />"
;
    } else {
        alert("updateTorrentImage: "+ fieldname +"-"+ tid);
    }
};