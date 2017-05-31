//Sets up the refresh when the page loads

$(document).ready(function ()
{
    //updateBuildTiles();
    // Refresh the tiles every minute.
    setInterval(function()
    {
        //alert("hi")
        updateTorrentsList('Refresh');
    }, 10000);

    $('#ajaxloader').hide();
});



// Ajax call for all torrent data

function updateTorrentsList(bulkaction)
{
    $.ajax({
        url: 'UpdateTorrentsList',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({'bulkaction': bulkaction}),
        dataType:'json',
        success: function(data)
        {
            updateAllTorrentTiles(data.torrents);
        }
    });
};




function updateAllTorrentTiles(torrentdatalist)
{
    $.each(torrentdatalist, function(index)
    {
        updateTorrentTile(torrentdatalist[index]);
    });
};



// Update the displayed data

function updateTorrentTile(dataitem)
{
    tid = dataitem.torrentid
    rerenderImage("StatusIcon-"+tid, "status_"+dataitem.status);
    rerenderText("Progress-"+tid, dataitem.progress)
};

