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
    $.getJSON(action+'Torrent='+pathname.substring(9))
        .done(function (data)
        {
                updateTorrentStateDisplay(data.selectedtorrent);
        });
};


// Ajax call for all torrent configuration data

function updateTorrentConfig(action)
{
    var pathname = window.location.pathname;
    $.getJSON('ReconfigureTorrent='+pathname.substring(9)+'='+action)
        .done(function (data)
        {
                updateTorrentConfigDisplay(data.selectedtorrent);
        });
};



// Ajax call for tv show seasons list

function updateTVShowSeasons(selectedseason)
{
    changeControlState('tvshowseasonselector', 'Hide');
    var tvshowname = getFieldValue("tvshowselector");
    if (tvshowname != "") {
        $.getJSON('GetTVShowSeasons='+tvshowname)
            .done(function (data)
            {
                    updateTVShowSeasonsList(data.seasons, selectedseason);
            });
    } else {
        updateTVShowSeasonsList("", selectedseason);
    };
    changeControlState('tvshowseasonselector', 'Show');
};


// Update the list of seasons in the dropdown list

function updateTVShowSeasonsList(seasonslist, selectedseason)
{
    repopulateDropDownList("tvshowseasonselector", seasonslist);
    setFieldValue('tvshowseasonselector', selectedseason)
};



// Update the displayed data

function updateTorrentStateDisplay(dataitem)
{
    rerenderImage("Status", "status_"+dataitem.status);
    rerenderText("Progress", dataitem.progress);
};



// Update the displayed data for configured data

function updateTorrentConfigDisplay(dataitem)
{
    rerenderText("TorrentTitle", dataitem.torrenttitle);
    rerenderImage("TorrentType", "type_"+dataitem.torrenttype);
    rerenderText("TorrentSubtitle", dataitem.torrentsubtitle);
};



// Edit torrent configuration

function editTorrentConfiguration()
{
    var moviename = getText('TorrentTitle')
    var movieyear = getText('TorrentSubtitle')
    var torrenttypeimagelabel = getImageName('TorrentType').substring(5);
    changeTorrentType(torrenttypeimagelabel);
    if (torrenttypeimagelabel == "movie") {
        setFieldValue('moviename', moviename);
        setFieldValue('movieyear', movieyear);
    } else if (torrenttypeimagelabel == "tvshow") {
        setFieldValue('tvshowselector', moviename);
        updateTVShowSeasons(movieyear);
    };
    changeAreasState('editmodefields', 'Show');
    changeAreasState('readonlyfields', 'Hide');
    changeControlState('Edit', 'Hide');
    changeControlState('Save', 'Show');
};


// Save torrent configuration

function saveTorrentConfiguration()
{
    var moviename = ""
    var movieyear = ""
    var newtype = ""
    if (getButtonState('MakeTVShow') == 'Disabled') {
        newtype = "tvshow";
    } else if (getButtonState('MakeMovie') == 'Disabled') {
        newtype = "movie";
    } else {
        newtype = "unknown";
    }
    if (newtype == 'tvshow') {
        moviename = getFieldValue("tvshowselector");
        movieyear = getFieldValue('tvshowseasonselector');
    } else if (newtype == 'movie') {
        moviename = getFieldValue("moviename");
        movieyear = getFieldValue('movieyear');
    } else {
        moviename = "New Unspecified Torrent";
        movieyear = "";
    };
    updateTorrentConfig(newtype+'|'+moviename+'|'+movieyear);
    changeAreasState('editmodefields', 'Hide');
    changeAreasState('readonlyfields', 'Show');
    changeControlState('Edit', 'Show');
    changeControlState('Save', 'Hide');
};


// Change torrent type

function changeTorrentType(newtype)
{
    if (newtype == "movie") {
        setFieldValue('moviename', '');
        setFieldValue('movieyear', '');
        changeAreasState('unknownonlyfields', "Hide");
        changeAreasState('tvshowonlyfields', "Hide");
        changeAreasState('movieonlyfields', "Show");
        changeButtonState('MakeMovie', "Disable");
        changeButtonState('MakeTVShow', "Enable");
        changeButtonState('MakeUnknown', "Enable");
    } else if (newtype == "tvshow") {
        setFieldValue('tvshowselector', '');
        setFieldValue('tvshowseasonselector', '');
        changeAreasState('unknownonlyfields', "Hide");
        changeAreasState('movieonlyfields', "Hide");
        changeAreasState('tvshowonlyfields', "Show");
        changeButtonState('MakeMovie', "Enable");
        changeButtonState('MakeTVShow', "Disable");
        changeButtonState('MakeUnknown', "Enable");
    } else {
        setFieldValue('moviename', '');
        setFieldValue('tvshowselector', '');
        setFieldValue('movieyear', '');
        setFieldValue('tvshowseasonselector', '');
        changeAreasState('unknownonlyfields', "Show");
        changeAreasState('tvshowonlyfields', "Hide");
        changeAreasState('movieonlyfields', "Hide");
        changeButtonState('MakeMovie', "Enable");
        changeButtonState('MakeTVShow', "Enable");
        changeButtonState('MakeUnknown', "Disable");
    };
};

// Change file designation

function changeFileDesignation(fileid, newtype)
{
    if (newtype == "ignore") {
        changeAreaState('copyconfig-'+fileid, "Hide");
        changeAreaState('ignoreconfig-'+fileid, "Show");
        changeButtonState('MakeIgnore-'+fileid, "Disable");
        changeButtonState('MakeCopy-'+fileid, "Enable");

    } else {
        changeAreaState('ignoreconfig-'+fileid, "Hide");
        changeAreaState('copyconfig-'+fileid, "Show");
        changeButtonState('MakeCopy-'+fileid, "Disable");
        changeButtonState('MakeIgnore-'+fileid, "Enable");
    };
};



function repopulateEpisodeLists(listmode)
{
    var newoptions = '';
    var liindex = 0;
    var liindexa = 0;
    if (listmode == "tvshow") {
        for (liindex = 1; liindex < 50; liindex++) {
            newoptions = newoptions + '<option value=\"'+liindex+'\">'+liindex+'</option>'
        }
        for (liindex = 1; liindex < 49; liindex++) {
            liindexa = liindex + 1
            newoptions = newoptions + '<option value=\"'+liindex+'-'+liindexa+'\">'+liindex+'-'+liindexa+'</option>'
        }
    } else {
        newoptions = newoptions + '<option value=\"Full\">Full</option>'
        newoptions = newoptions + '<option value=\"Part 1\">Part 1</option>'
        newoptions = newoptions + '<option value=\"Part 2\">Part 2</option>'
        newoptions = newoptions + '<option value=\"Part 3\">Part 3</option>'
    };
    var ddobjectlist = document.getElementsByClass('episodeselector');
    var ddindex;
    for (ddindex = 0; ddindex < ddobjectlist.length; ddindex++) {
        ddobject = ddobjectlist[ddindex];
        ddobject.innerHTML = newoptions;
    };
};
