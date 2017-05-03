
// Ajax call for all torrent configuration data

function updateTorrentConfig(action)
{
    var pathname = window.location.pathname;
    $.ajax({
        url: 'ReconfigureTorrent='+pathname.substring(9),
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(action),
        dataType:'json',
        success: function(data){
            updateTorrentConfigDisplay(data.selectedtorrent);
        }
    });
};



// Update the displayed data for configured data

function updateTorrentConfigDisplay(dataitem)
{
    rerenderText("TorrentTitle", dataitem.torrenttitle);
    rerenderText("TorrentSubtitlePrefix", dataitem.torrenttitleseparator);
    rerenderText("TorrentSubtitle", dataitem.torrentsubtitle);
    rerenderText("TorrentSubtitleEnd", dataitem.torrentsubtitleend);
    rerenderImage("TorrentType", "type_"+dataitem.torrenttype);

    var filelist = dataitem.files;
    $.each(filelist, function(index)
    {
        rerenderText("fileseason-"+filelist[index].fileid, filelist[index].fileseason);
        rerenderText("fileepisode-"+filelist[index].fileid, filelist[index].fileepisode);
        rerenderText("filesubtitle-"+filelist[index].fileid, filelist[index].filesubtitle);
        rerenderImage("outcome-"+filelist[index].fileid, "fileaction_"+filelist[index].outcome);
    });

};


