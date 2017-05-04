//Sets up the refresh when the page loads

$(document).ready(function ()
{
    changeControlState('Edit', 'Show');

    // Refresh the tiles every minute.
    setInterval(function()
    {
        updateTorrentState('Refresh');
    }, 10000);
});



// Ajax call for all torrent downloading data

function updateTorrentState(action)
{
    var pathname = window.location.pathname;
    $.ajax({
        url: 'UpdateTorrent='+pathname.substring(9),
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({'torrentaction': action}),
        dataType:'json',
        success: function(data)
        {
            updateTorrentStateDisplay(data.selectedtorrent);
        }
    });
};



// Update the displayed data

function updateTorrentStateDisplay(dataitem)
{
    rerenderImage("Status", "status_"+dataitem.status);
    rerenderText("Progress", dataitem.progress);
};


