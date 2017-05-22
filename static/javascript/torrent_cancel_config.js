
// Cancel Edit torrent configuration

function cancelTorrentConfiguration()
{
    changeAreasState('editmodefields', 'Hide');
    changeAreasState('readonlyfields', 'Show');
    changeButtonState('Edit', 'Show');
    changeButtonState('Save', 'Hide');
    changeButtonState('Cancel', 'Hide');
    changeButtonState('Exit', 'Show');
    changeButtonState('Copy', 'Show');
    changeButtonState('Delete', 'Show');
};
