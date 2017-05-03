
// Call for to add torrent

function addTorrent()
{
    var newurl = getFieldValue('newurl');
    window.location.replace("/AddTorrent="+newurl);
};
