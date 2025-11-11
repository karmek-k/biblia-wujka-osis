from datetime import date


class OsisExport:
    def __init__(self, *, publication_date: date=date.today()):
        self.template = self.template(
            publication_date=publication_date,
        )

    @staticmethod
    def template(*, publication_date: date) -> str:
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
</osisText>
</osis>"""

