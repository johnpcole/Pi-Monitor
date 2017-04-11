//Sets up the refresh when the page loads

$(document).ready(function ()
{
    rerenderControl('Edit', 'Show');

    // Refresh the tiles every minute.
    setInterval(function()
    {
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
            if (action == 'Refresh') {
                updateTorrentTile(data.selectedtorrent);
            } else {
                updateTorrentConfig(data.selectedtorrent);
            };
        });
};



// Update the displayed data

function updateTorrentTile(dataitem)
{
    rerenderImage("Status", dataitem.status, "tilesubicon");
    rerenderText("Progress", dataitem.progress);
    rerenderText("SizeEta", "of "+dataitem.sizeeta);
};



// Update the displayed data for configured data

function updateTorrentConfig(dataitem)
{
    rerenderText("Sanitisedname", dataitem.sanitisedname);
};



// Edit torrent configuration

function editTorrentConfiguration()
{
    var itemdetails = getText('Sanitisedname');
    var itemsplit = itemdetails.split("   (");
    var moviename = itemsplit[0];
    var itemsplit = itemsplit[1].split(")");
    var movieyear = itemsplit[0];
    setFieldValue('moviename', moviename);
    setFieldValue('movieyear', movieyear);
    rerenderArea('edittextfields', 'Show');
    rerenderControl('Edit', 'Hide');
    rerenderControl('Save', 'Show');
};


// Save torrent configuration

function saveTorrentConfiguration()
{
    
    var moviename = getFieldValue('moviename');
    var movieyear = getFieldValue('movieyear');
    updateTorrent('Reconfigure|'+moviename+"|"+movieyear);
    rerenderArea('edittextfields', 'Hide');
    rerenderControl('Edit', 'Show');
    rerenderControl('Save', 'Hide');
};



