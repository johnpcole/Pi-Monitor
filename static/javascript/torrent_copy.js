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
                var outputtext = '<div class="dialogtitle">Copying Files...</div><div class="dialogsplitter"></div>'
                $.each(copydata, function(index)
                {
                    var currentitem = copydata[index]
                    outputtext = outputtext + '<div class="dialogitemleft dialogitem">' + currentitem.description + '</div>'
                    outputtext = outputtext + '<div class="dialogitemright dialogitem"><img src="./static/images/copy_'
                    outputtext = outputtext + currentitem.status + '.png" alt="copy" /></div>'
                });
                rerenderText('dialogcontent', outputtext)
            } else {
                //$('#copydialog').hide()
            };
        }
    });
};
