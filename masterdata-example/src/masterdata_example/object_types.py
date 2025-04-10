from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment
from bam_masterdata.metadata.entities import ObjectType


class TensileTestingMachine(TestingMachine):
    defs = ObjectTypeDef(
        code="TENSILE_TESTING_MACHINE",
        description="""
        A machine designed to perform tensile tests, probably according to a specific standard.//Eine Prüfmaschine, mit der Zugversuche durchgeführt werden können, ggf. im Zusammenhang mit bestimmten Normen.
        """,
        iri="https://w3id.org/pmd/co/PMD_0000973",
        generated_code_prefix="INS.TMACH.TTM",
    )

    max_extensometer_length = PropertyTypeAssignment(
        code="MAX_EXTENSOMETER_LENGTH",
        data_type="REAL",
        property_label="Maximum Extensometer Length [mm]",
        description="""Maximum extensometer length due to physical restriction of the extensometer device attached to the tensile testing machine//Maximale Extensometerlänge, die sich an der physischen Grenze des angeschlossenen Extensometers orientiert""",
        mandatory=False,
        show_in_edit_views=False,
        section="Machine Details",
    )

    max_load = PropertyTypeAssignment(
        code="MAX_LOAD",
        data_type="REAL",
        property_label="Maximum Load [kN]",
        description="""Maximum usable load due to physical restriction of the load cell attached to the tensile testing machine//Maximale Lastaufbringung, die sich an der physischen Grenze der angeschlossenen Kraftmessdose orientiert""",
        mandatory=False,
        show_in_edit_views=False,
        section="Machine Details",
    )

    # see `vocabulary_types.py` for the definition of this CONTROLLEDVOCABULARY
    controlled_name = PropertyTypeAssignment(
        code="CONTROLLED_NAME",
        data_type="CONTROLLEDVOCABULARY",
        property_label="Controlled Name",
        description="""A controlled and well-defined name for the example object type//Ein kontrollierter und wohldefinierter Name für den Beispielobjekttyp""",
        mandatory=False,
        show_in_edit_views=False,
        section="General Information",
    )
