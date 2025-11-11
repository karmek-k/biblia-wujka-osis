from datetime import date

from extract.books import Book


class OsisExport:
    def __init__(self, *, publication_date: date=date.today()):
        self.publication_date = publication_date
    
    def export(self, books: list[Book]) -> str:
        result = []        

        for book in books:
            book_name = translate_book_name(book.name)
            result += f"<div type='book' osisID='{book_name}'>"

            # process chapters
            for i_chapter, chapter in enumerate(book.chapters, 1):
                result += f"<chapter osisID='{book_name}.{i_chapter}'>"

                chapter.parse()
                result += f"<title>{chapter.title}</title>"

                # chapter.verses is a dictionary
                for i_verse, verse in chapter.verses.items():
                    result += f"<verse osisID='{book_name}.{i_chapter}.{i_verse}'>{verse}</verse>"

                result += "</chapter>"

            result += "</div>"

        return self.template(''.join(result), publication_date=self.publication_date)

    @staticmethod
    def template(content: str, *, publication_date: date) -> str:
        return f"""<?xml version='1.0' encoding='UTF-8'?>
<osis xsi:schemaLocation='http://www.bibletechnologies.net/2003/OSIS/namespace http://www.bibletechnologies.net/osisCore.2.1.1.xsd' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xmlns='http://www.bibletechnologies.net/2003/OSIS/namespace'>
<osisText osisRefWork='Bible' osisIDWork='BWujka' xml:lang='pl'>
    <header>
    <work osisWork='BWujka'>
        <title>Biblia Jakuba Wujka</title>
        <contributor>Bartosz Gleń</contributor>
        <date>{publication_date.isoformat()}</date>
        <description>Biblia Jakuba Wujka wydana przez Brytyjskie i Zagraniczne Towarzystwo Biblijne w 1923 roku. Kanon protestancki, bez ksiąg deuterokanonicznych.</description>
        <publisher>Bartosz Gleń</publisher>
        <type type='OSIS'>Bible</type>
        <identifier type='OSIS'>BWujka</identifier>
        <source>https://pl.wikisource.org/wiki/Biblia_Wujka_(1923)</source>
        <language type='IETF'>pl</language>
        <rights>Public Domain</rights>
        <refSystem>Bible</refSystem>
    </work>
    </header>
    {content}
</osisText>
</osis>"""


def translate_book_name(title: str) -> str:
    titles = {
        # Old Testament
        'Genesis, to jest pierwsze': 'Gen',
        'Exodus, to jest wtóre': 'Exod',
        'Leviticus, to jest trzecie': 'Lev',
        'Numeri, to jest czwarte': 'Num',
        'Deuteronomium, to jest piąte': 'Deut',
        'Jozue': 'Josh',
        'Sędziów': 'Judg',
        'Ruth': 'Ruth',
        'Królewskie pierwsze (Samuelowe I)': '1Sam',
        'Królewskie drugie (Samuelowe II)': '2Sam',
        'Królewskie trzecie (Królewskie I)': '1Kgs',
        'Królewskie czwarte (Królewskie II)': '2Kgs',
        'Paralipomenon pierwsze': '1Chr',
        'Paralipomenon wtóre': '2Chr',
        'Ezdraszowe (pierwsze)': 'Ezra',
        'Nehemiaszowe (Ezdraszowe wtóre)': 'Neh',
        'Esther': 'Esth',
        'Job': 'Job',
        'Księgi Psalmów': 'Ps',
        'Przypowieści': 'Prov',
        'Ekklesiastes': 'Eccl',
        'Pieśń nad pieśniami': 'Song',
        'Izajasz prorok': 'Isa',
        'Jeremiasz': 'Jer',
        'Threny Jeremiasza': 'Lam',
        'Ezechiel prorok': 'Ezek',
        'Daniel': 'Dan',
        'Ozeasz': 'Hos',
        'Joel': 'Joel',
        'Amos': 'Amos',
        'Abdyasz': 'Obad',
        'Jonas': 'Jonah',
        'Micheasz': 'Mic',
        'Nahum': 'Nah',
        'Habakuk': 'Hab',
        'Sophoniasz': 'Zeph',
        'Aggeusz': 'Hag',
        'Zacharyasz': 'Zech',
        'Malachyasz': 'Mal',

        # New Testament
        'Ewangelia św. Mateusza': 'Matt',
        'Ewangelia św. Marka': 'Mark',
        'Ewangelia św. Łukasza': 'Luke',
        'Ewangelia św. Jana': 'John',
        'Dzieje Apostolskie': 'Acts',
        'List św. Pawła do Rzymian': 'Rom',
        'List pierwszy św. Pawła do Korynthów': '1Cor',
        'List wtóry św. Pawła do Korynthów': '2Cor',
        'List św. Pawła do Galatów': 'Gal',
        'List św. Pawła do Ephezów': 'Eph',
        'List św. Pawła do Philippensów': 'Phil',
        'List św. Pawła do Kolossan': 'Col',
        'List pierwszy św. Pawła do Thessaloniczan': '1Thess',
        'List wtóry św. Pawła do Thessaloniczan': '2Thess',
        'List pierwszy św. Pawła do Tymotheusza': '1Tim',
        'List wtóry św. Pawła do Tymotheusza': '2Tim',
        'List św. Pawła do Tytusa': 'Titus',
        'List św. Pawła do Philemona': 'Phlm',
        'List św. Pawła do Żydów': 'Heb',
        'List św. Jakóba': 'Jas',
        'List pierwszy św. Piotra': '1Pet',
        'List wtóry św. Piotra': '1Pet',
        'List pierwszy św. Jana': '1John',
        'List wtóry św. Jana': '2John',
        'List trzeci św. Jana': '3John',
        'List św. Judy': 'Jude',
        'Objawienie św. Jana': 'Rev',
    }

    if title not in titles.keys() or titles[title] is None:
        raise Exception(f'No translation defined for {title}')
    
    return titles[title]