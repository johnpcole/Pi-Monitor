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
                updateTorrentState(data.selectedtorrent);
            } else {
                updateTorrentConfig(data.selectedtorrent);
            };
        });
};



// Update the displayed data

function updateTorrentState(dataitem)
{
    rerenderImage("Status", dataitem.status);
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
    var torrenttypeimagelabel = getImageName('torrenttypeimage');
    changeTorrentType(torrenttypeimagelabel);
    setFieldValue('moviename', moviename);
    setFieldValue('tvshowselector', moviename);
    setFieldValue('movieyear', movieyear);
    rerenderArea('edittextfields', 'Show');
    rerenderControl('MakeUnknown', 'Show');
    rerenderControl('MakeMovie', 'Show');
    rerenderControl('MakeTVShow', 'Show');
    rerenderControl('Edit', 'Hide');
    rerenderControl('Save', 'Show');
};


// Save torrent configuration

function saveTorrentConfiguration()
{
    var torrenttype = getImageName('torrenttypeimage');
    var moviename = getFieldValue('moviename');
    var movieyear = getFieldValue('movieyear');
    updateTorrent('Reconfigure|'+torrenttype+'|'+moviename+'|'+movieyear);
    rerenderArea('edittextfields', 'Hide');
    rerenderControl('Edit', 'Show');
    rerenderControl('Save', 'Hide');
};


// Change torrent type

function changeTorrentType(newtype)
{
    if (newtype == "movie") {
        rerenderControl('tvshowselector', "Hide");
        rerenderControl('moviename', "Show");
        rerenderControl('movieyear', "Show");
        rerenderControl('MakeMovie', "Disable");
        rerenderControl('MakeTVShow', "Enable");
        rerenderControl('MakeUnknown', "Enable");
    } else if (newtype == "tvshow") {
        rerenderControl('tvshowselector', "Show");
        rerenderControl('moviename', "Hide");
        rerenderControl('movieyear', "Show");
        rerenderControl('MakeMovie', "Enable");
        rerenderControl('MakeTVShow', "Disable");
        rerenderControl('MakeUnknown', "Enable");
    } else {
        rerenderControl('tvshowselector', "Hide");
        rerenderControl('moviename', "Hide");
        rerenderControl('movieyear', "Hide");
        rerenderControl('MakeMovie', "Enable");
        rerenderControl('MakeTVShow', "Enable");
        rerenderControl('MakeUnknown', "Disable");
    };
    rerenderImage('torrenttypeimage', newtype);
};