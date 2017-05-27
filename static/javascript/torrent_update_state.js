//Sets up the refresh when the page loads

$(document).ready(function ()
{
    changeButtonState('Edit', 'Show');
    changeButtonState('Save', 'Hide');
    changeButtonState('Cancel', 'Hide');
    updateStartStopButtons(getImageName('Status').substr(8));

    // Refresh the tiles every minute.
    setInterval(function()
    {
        updateTorrentState('Refresh');
    }, 10000);

    $('#ajaxloader').hide();
});



// Ajax call for all torrent downloading data

function updateTorrentState(action)
{
    var pathname = window.location.pathname;
    var torrentid = pathname.substring(9)
    $.ajax({
        url: 'UpdateTorrent',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({'torrentid':torrentid, 'torrentaction':action}),
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
    updateStartStopButtons(dataitem.status);
};



function updateStartStopButtons(torrentstate)
{
    suffix = torrentstate.substr(torrentstate.length-6);
    if (suffix == "active") {
        changeButtonState('Start', 'Hide');
        changeButtonState('Stop', 'Show');
    } else if (suffix == "queued") {
        changeButtonState('Start', 'Hide');
        changeButtonState('Stop', 'Show');
    } else if (suffix == "paused"){
        changeButtonState('Stop', 'Hide');
        changeButtonState('Start', 'Show');
    } else {
        changeButtonState('Stop', 'Hide');
        changeButtonState('Start', 'Hide');
    };
};