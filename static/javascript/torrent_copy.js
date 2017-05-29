// Invoke Torrent File Copy

function copyTorrent()
{
    var pathname = window.location.pathname;
    var torrentid = pathname.substring(9)
    changeButtonState('CloseCopy',"Disable")
    $('#copydialog').show()
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
                var outputtext = ''
                $.each(copydata, function(index)
                {
                    var currentitem = copydata[index]
                    outputtext = outputtext + '<div class="dialogitemleft dialogitem">' + currentitem.description + '</div>'
                    outputtext = outputtext + '<div class="dialogitemright dialogitem"><img src="./static/images/copy_'
                    outputtext = outputtext + currentitem.status + '.png" alt="copy" /></div>'
                });
                rerenderText('dialogcontent', outputtext)
            if (data.refreshmode == true) {
                interactTorrentCopy("!!! CONTINUE EXISTING COPY PROCESS !!!")
            } else {
                changeButtonState('CloseCopy',"Enable")
            };
        }
    });
};


// Close torrent copy dialog

function closeCopyDialog()
{
    $('#copydialog').hide()
};
