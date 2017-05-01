//Sets up the refresh when the page loads

$(document).ready(function ()
{
    //updateBuildTiles();
    // Refresh the tiles every minute.
    setInterval(function()
    {
        //alert("hi")
        updateTorrentsList();
    }, 10000);
});



// Ajax call for all torrent data

function updateTorrentsList()
{
    $.getJSON('UpdateTorrentsList')
        .done(function (data)
        {
            var torrentlist = data.torrents;
            $.each(torrentlist, function(index)
            {
                updateTorrentTile(torrentlist[index]);
            });
        });
};



// Update the displayed data

function updateTorrentTile(dataitem)
{
    tid = dataitem.torrentid
    rerenderImage("StatusIcon-"+tid, "status_"+dataitem.status);
    rerenderText("Progress-"+tid, dataitem.progress)
};

