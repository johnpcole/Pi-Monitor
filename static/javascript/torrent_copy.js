// Edit torrent configuration

function copyTorrent()
{
    $('#copydialog').show()
    var pathname = window.location.pathname;
    var torrentid = pathname.substring(9)
    interactTorrentCopy(torrentid)
};


// Ajax call to get default edit fields

function interactTorrentCopy(torrentid)
{
    $.ajax({
        url: 'CopyTorrent',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({'copyinstruction':torrentid}),
        dataType:'json',
        success: function(data){
            var copydata = data.copydata
            if (data.refreshmode == true) {
                interactTorrentCopy("!!! CONTINUE EXISTING COPY PROCESS !!!")
                var outputtext = ""
                $.each(copydata, function(index)
                {
                    var currentitem = copydata[index]
                    outputtext = outputtext + "<p>" + currentitem.description + "</p>"
                    outputtext = outputtext + "<p>" + currentitem.status + "</p>"
                });
                rerenderText('copydialog', outputtext)
            } else {
                $('#copydialog').hide()
            };
        }
    });
};

