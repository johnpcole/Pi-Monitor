// Edit torrent configuration

function editTorrentConfiguration()
{
    getTorrentConfig()
    changeAreasState('editmodefields', 'Show');
    changeAreasState('readonlyfields', 'Hide');
    changeControlState('Edit', 'Hide');
    changeControlState('Save', 'Show');
};


// Ajax call to get default edit fields

function getTorrentConfig()
{
    var pathname = window.location.pathname;
    $.getJSON('EditTorrent='+pathname.substring(9))
        .done(function (data)
        {
            updateTorrentConfigFields(data.selectedtorrent, data.listitems);
        });
};


// Update the edit fields for configured data

function updateTorrentConfigFields(editinfo, listitems)
{
    changeTorrentType(editinfo.torrenttype);
    setFieldValue('moviename', editinfo.moviename);
    setFieldValue('movieyear', editinfo.movieyear);
    repopulateDropDownList('tvshowselector', listitems.tvshows)
    setDropDownValue('tvshowselector', editinfo.tvshowname);
    updateTVShowSeasons(editinfo.tvshowseason);
    var filelist = editinfo.files;
    $.each(filelist, function(index)
    {
        var currentfile = filelist[index]
        changeFileDesignation(index, currentfile.outcome);
        populateFileDropDownLists(currentfile.filetype, index, listitems)
        if (currentfile.outcome == "copy") {
            if (editinfo.torrenttype == "tvshow") {
                setDropDownValue('episodeselector-'+index, currentfile.episodeselector);
            };
            if (currentfile.filetype == "subtitle") {
                setDropDownValue('subtitleselector-'+index, currentfile.subtitleselector);
            };
        };
    });
};


// Populate the file drop-down lists

function populateFileDropDownLists(filetype, fileindex, listitems)
{
    if (filetype != "none") {
        repopulateDropDownList('episodeselector-'+fileindex, listitems.episodes);
        if (filetype == "subtitle") {
            repopulateDropDownList('subtitleselector-'+fileindex, listitems.subtitles)
        };
    };
};
