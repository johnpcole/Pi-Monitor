//Sets up the refresh when the page loads

$(document).ready(function ()
{
    updateStartStopButtons(getImageName('Status').substr(8));
    changeAreasState('readmodebuttons', 'Show');

    // Refresh the tiles every minute.
    setInterval(function()
    {
        if ((getAreaState('copydialog') == 'Hidden') && (getAreaState('deletedialog') == 'Hidden')) {
            updateTorrentState('Refresh');
        };
    }, 10000);

    $('#ajaxloader').hide();
});


// Return the current torrent id

function getCurrentTorrentId()
{
    var pathname = window.location.pathname;
    var torrentid = pathname.substring(9);
    return torrentid;
};


// Ajax call for all torrent downloading data

function updateTorrentState(action)
{
    $.ajax({
        url: 'UpdateTorrent',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({'torrentid':getCurrentTorrentId(), 'torrentaction':action}),
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
    updateCopyButton(dataitem.status);
};


