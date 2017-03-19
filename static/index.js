//Sets up the refresh when the page loads

$(document).ready(function ()
{
    //updateBuildTiles();
    // Refresh the tiles every minute.
    setInterval(function()
    {
        //alert("hi")
        updateTorrentInfo();
    }, 10000);
});



// Ajax call for all torrent data

function updateTorrentInfo()
{
    $.getJSON('UpdateData')
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
        updateTorrentData(tid, "Eta", dataitem.eta);
        updateTorrentData(tid, "Progress", dataitem.progress);
        updateTorrentData(tid, "Status", dataitem.status);
        updateTorrentData(tid, "Finished", dataitem.finished);
    } else {
        alert(dataitem.torrentid);
    }
};


// Update the displayed data value

function updateTorrentData(tid, fieldname, fieldvalue)
{
    var tileData = document.getElementById(fieldname+"-"+tid);
    if (tileData != null) {
        tileData.innerHTML = fieldvalue;
    } else {
        alert(fieldname+"-"+tid);
    }
};