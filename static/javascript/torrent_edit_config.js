// Edit torrent configuration

function editTorrentConfiguration()
{
    getTorrentConfig()
    changeAreasState('editmodefields', 'Show');
    changeAreasState('readonlyfields', 'Hide');
    changeButtonState('Edit', 'Hide');
    changeButtonState('Save', 'Show');
    changeButtonState('Cancel', 'Show');
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
        changeFileDesignation(currentfile.fileid, currentfile.outcome);
        populateFileDropDownLists(currentfile.filetype, currentfile.fileid, listitems)
        if (currentfile.outcome == "copy") {
            if (editinfo.torrenttype == "tvshow") {
                setDropDownValue('episodeselector-'+currentfile.fileid, currentfile.episodeselector);
            };
            if (currentfile.filetype == "subtitle") {
                setDropDownValue('subtitleselector-'+currentfile.fileid, currentfile.subtitleselector);
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
