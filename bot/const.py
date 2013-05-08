import pywikibot as wp


WIKIDATA = wp.Site('wikidata', 'wikidata')
WIKIDATA_DATASITE = WIKIDATA.data_repository()


ARTIST_MBID_PID = 'P434'
WORK_MBID_PID = 'P435'
RELEASE_GROUP_MBID_PID = 'P436'
LABEL_MBID_PID = None


MB_WIKI_ARTIST_LINK_ID = 179
MB_WIKI_ALBUM_LINK_ID = 89
MB_WIKI_LABEL_LINK_ID = 216
MB_WIKI_WORK_LINK_ID = 279


MUSICBRAINZ_WIKIDATAPAGE = wp.ItemPage(WIKIDATA_DATASITE, "Q14005")
MUSICBRAINZ_CLAIM = wp.Claim(WIKIDATA, "P143")
MUSICBRAINZ_CLAIM.setTarget(MUSICBRAINZ_WIKIDATAPAGE)