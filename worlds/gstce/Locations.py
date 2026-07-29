from BaseClasses import Location
from typing import Dict, List, TypeVar, NamedTuple, Optional

class GuacLocation(Location):
    game: str = "Guacamelee Super Turbo Champioship Edition"

class GuacLocationData(NamedTuple):
    id: int
    area: str
    name: str
    region: str
    type: str

location_table: List[GuacLocationData] = {
    # Temple of Rain 1-50
    GuacLocationData(1, "ToR", "Goat Jump Puzzle Chest", "Temple of Rain", "chest"),
    GuacLocationData(2, "ToR", "Near Entrance Omlec Chest", "Temple of Rain", "chest"),
    GuacLocationData(3, "ToR", "Omlec Wing Standalone Chest", "Temple of Rain", "chest"),
    GuacLocationData(4, "ToR", "Near Netrance Jump Puzzle Chest", "Temple of Rain", "chest"),
    GuacLocationData(5, "ToR", "Heart Chest Room 1", "Temple of Rain", "chest"),
    GuacLocationData(6, "ToR", "Heart Chest Room 2", "Temple of Rain", "chest"),
    GuacLocationData(7, "ToR", "Heart Chest Room 3", "Temple of Rain", "chest"),
    GuacLocationData(8, "ToR", "Heart Chest Room 4", "Temple of Rain", "chest"),
    GuacLocationData(9, "ToR", "Heart Chest Room 5", "Temple of Rain", "chest"),
    GuacLocationData(10, "ToR", "Heart Chest Room 6", "Temple of Rain", "chest"),
    GuacLocationData(11, "ToR", "Shortcut Chest", "Temple of Rain", "chest"),
    GuacLocationData(12, "ToR", "Before Alrbrije Chase Chest", "Temple of Rain", "chest"),
    GuacLocationData(13, "ToR", "After Alrbrije Chase Chest", "Temple of Rain", "chest"),
    GuacLocationData(14, "ToR", "Near Luchita Chest", "Temple of Rain", "chest"),

    # Forest del Chivo 50-99
    GuacLocationData(51, "FdC", "Near Pueblucho Chest", "Forest Upper Left", "chest"),
    GuacLocationData(52, "FdC", "Lower Pollo Chest", "Forest Upper Right", "chest"),
    GuacLocationData(53, "FdC", "Near Chivo Store Chest", "Forest Upper Right", "chest"),
    GuacLocationData(54, "FdC", "Alcove Near Luchita Chest", "Forest Upper Right", "chest"),
    GuacLocationData(55, "FdC", "Main Shaft Red Challenge Chest", "Forest Shaft", "chest"),
    GuacLocationData(56, "FdC", "Main Shaft Yellow Challenge Chest", "Forest Shaft", "chest"),
    GuacLocationData(57, "FdC", "Main Shaft Blue Challenge Chest", "Forest Shaft", "chest"),
    GuacLocationData(58, "FdC", "Near Tule Tree Chest", "Forest Bottom", "chest"),
    GuacLocationData(59, "FdC", "Chivo Alcove Chest", "Forest Choozo", "chest"),
    GuacLocationData(60, "FdC", "Chivo Pollo Chest", "Forest Choozo", "chest"),
    GuacLocationData(61, "FdC", "Main Shaft Green Challenge Chest", "Forest Shaft", "chest"),
    GuacLocationData(62, "FdC", "Skull Lever Chest", "Forest Choozo", "chest"),
    GuacLocationData(63, "FdC", "High Platform Chest", "Forest Choozo", "chest"),
    GuacLocationData(64, "FdC", "Near Canal Chest", "Forest Shaft", "chest"),

    # Tule Tree 101-150
    GuacLocationData(101,"TT","4F Outside Chest", "Tule Tree", "chest"),
    GuacLocationData(102,"TT","5F Inside Chest", "Tule Tree", "chest"),
    GuacLocationData(103,"TT","9F Outside Chest", "Tule Tree", "chest"),
    GuacLocationData(104,"TT","12F Fight Chest", "Tule Tree", "chest"),
    GuacLocationData(105,"TT","12F Pollo Chest", "Tule Tree","chest"),
    GuacLocationData(106,"TT","12F Jump Puzzle Chest", "Tule Tree","chest"),
    GuacLocationData(107,"TT","6F Outside Chest", "Tule Tree","chest"),
    GuacLocationData(108,"TT","13F Outside Chest", "Tule Tree","chest"),

    # Sierra Morena 151-200
    GuacLocationData(151,"SM","Near Upper Pico De Gallo Chest","Sierra Morena","chest"),
    GuacLocationData(152,"SM","Near Luchita Chest","Sierra Morena","chest"),
    GuacLocationData(153,"SM","Dimension Swap Climb Chest","Sierra Morena","chest"),
    GuacLocationData(154,"SM","Near Lower Pico De Gallo Chest","Sierra Morena","chest"),
    GuacLocationData(155,"SM","Hidden Goat Fly Chest","Sierra Morena","chest"),
    GuacLocationData(156,"SM","Hidden Goat Fly And Climb Chest","Sierra Morena","chest"),
    GuacLocationData(157,"SM","Near Great Temple Lower Chest","Sierra Morena","chest"),
    GuacLocationData(158,"SM","Near Great Temple Upper Chest","Sierra Morena","chest"),

    # Pueblucho 201-250
    GuacLocationData(201, "Pb", "Outside Church Chest","Peublucho", "chest"),
    GuacLocationData(202, "Pb", "Pollo Chest","Peublucho", "chest"),
    GuacLocationData(203, "Pb", "X'tabay Chest","Peublucho", "chest"),
    GuacLocationData(204, "Pb", "Inside Church Chest","Peublucho", "chest"),

    # Great Temple 251-300
    GuacLocationData(251,"GT","Pollo Maze Chest","Great Temple","chest"),
    GuacLocationData(252,"GT","Near Entrance Jump Puzzle Chest","Great Temple","chest"),
    GuacLocationData(253,"GT","Goat Fly Puzzle Chest","Great Temple","chest"),
    GuacLocationData(254,"GT","Pollo Hole Chest","Great Temple","chest"),
    GuacLocationData(255,"GT","Alux Fight Chest","Great Temple","chest"),
    GuacLocationData(256,"GT","Barrel Room Near Sierra Chest","Great Temple","chest"),
    GuacLocationData(257,"GT","WarpMazeChest","Great Temple","chest"),

    # Temple of War 301-350
    GuacLocationData(301,"ToW","Dead End Chest","Temple of War","chest"),
    GuacLocationData(302,"ToW","Pollo Hole Chest","Temple of War","chest"),
    GuacLocationData(303,"ToW","Cactus Jump Puzzle Chest","Temple of War","chest"),
    GuacLocationData(304,"ToW","After Flame Face Chest","Temple of War","chest"),
    GuacLocationData(305,"ToW","Goat Climb Chute Chest","Temple of War","chest"),
    GuacLocationData(306,"ToW","Wall Slide Puzzle Chest","Temple of War","chest"),
    GuacLocationData(307,"ToW","Blue Block Jump Puzzle Chest","Temple of War","chest"),
    GuacLocationData(308,"ToW","Halfway Blue Block Chest","Temple of War","chest"),
    GuacLocationData(309,"ToW","Cactus Exploder Fight Chest","Temple of War","chest"),
    GuacLocationData(310,"ToW","Upper Side Room Chest","Temple of War","chest"),
    GuacLocationData(311,"ToW","Upper Jump Puzzle Chest","Temple of War","chest"),
    GuacLocationData(312,"ToW","Entrance Pollo Bomba Chest","Temple of War","chest"),

    # Caverna del Pollo 351-400
    GuacLocationData(351, "CdP", "Challegne 1 Chest","Caverna del Pollo", "chest"),
    GuacLocationData(352, "CdP", "Challegne 2 Left Chest","Caverna del Pollo", "chest"),
    GuacLocationData(353, "CdP", "Challegne 2 Right Chest","Caverna del Pollo", "chest"),

    #La Mansion del Presidente 400
    GuacLocationData(400, "LmdP", "Platform Chest","Mansion", "chest"),

    # Agave Field
    GuacLocationData(401, "AF", "Juan House Chest", "Agave Field", "chest"),

    # Santa Luchita 451-500
    GuacLocationData(451, "SL", "Upper Inn Chest","Santa Luchita", "chest"),
    GuacLocationData(452, "SL", "Lower Inn Chest","Santa Luchita", "chest"),
    GuacLocationData(453, "SL", "Hernandos Chest","Santa Luchita", "chest"),
    GuacLocationData(454, "SL", "Hernandos Pollo Chest","Santa Luchita", "chest"),
    GuacLocationData(455, "SL", "Near Caverna Chest","Santa Luchita", "chest"),

    #Canal de las Flores 501-550
    GuacLocationData(501, "CdlF", "Near Forest Left Chest","Canal", "chest"),
    GuacLocationData(502, "CdlF", "Near Forest Right Chest","Canal", "chest"),
    GuacLocationData(503, "CdlF", "Path to Bridge Chest","Canal", "chest"),
    GuacLocationData(504, "CdlF", "Pollo Bomba West of Tower Chest","Canal", "chest"),
    GuacLocationData(505, "CdlF", "Pollo Dimension Maze Chest","Canal", "chest"),
    GuacLocationData(506, "CdlF", "Pollo Hole Chest","Canal", "chest"),
    GuacLocationData(507,"CdlF", "Town Chest","Canal", "chest"),
    GuacLocationData(508, "CdlF", "Near Choozo Chest","Canal", "chest"),
    GuacLocationData(509, "CdlF", "Above Town Chest","Canal", "chest"),
    GuacLocationData(510, "CdlF", "East of Town Chest","Canal", "chest"),
    GuacLocationData(511, "CdlF", "Right of Ferry Chest","Canal", "chest"),
    GuacLocationData(512, "CdlF", "Above Ferry Chest","Canal", "chest"),
    GuacLocationData(513, "CdlF", "West of Town Chest","Canal", "chest"),
    GuacLocationData(514, "CdlF", "Near Pico de Gallo Chest","Canal", "chest"),
    GuacLocationData(515, "CdlF", "Bridge Jump Puzzle Chest","Canal", "chest"),
    GuacLocationData(516, "CdlF", "Above Bridge Chest","Canal", "chest"),
    GuacLocationData(517,"CdlF","Clubhouse Top Chest","Canal","chest"),
    GuacLocationData(518,"CdlF","Clubhouse Bottom Left Chest","Canal","chest"),
    GuacLocationData(519,"CdlF","Clubhouse Bottom Right Chest","Canal","chest"),

    # Pico de Gallo 551-600
    GuacLocationData(551,"PdG","Lava Goat Fly Passage High Chest","Pico de Gallo","chest"),
    GuacLocationData(552,"PdG","Chute Chest","Pico de Gallo","chest"),
    GuacLocationData(553,"PdG","Outside Above Entrance Chest","Pico de Gallo","chest"),
    GuacLocationData(554,"PdG","Destroyed Town Chest","Pico de Gallo","chest"),
    GuacLocationData(555,"PdG","Dashing Derpderp Passage Chest","Pico de Gallo","chest"),
    GuacLocationData(556,"PdG","Pollo Bomba Jump Puzzle Chest","Pico de Gallo","chest"),
    GuacLocationData(557,"PdG","Pollo Bomba Chest","Pico de Gallo","chest"),
    GuacLocationData(558,"PdG","Lava Goat Fly Passage Low Chest","Pico de Gallo","chest"),
    GuacLocationData(559,"PdG","Inside Near Entrance Pollo Chest","Pico de Gallo","chest"),
    GuacLocationData(560,"PdG","Skeleton Room Chest","Pico de Gallo","chest"),
    GuacLocationData(561,"PdG","Near Choozo Chest","Pico de Gallo","chest"),
    GuacLocationData(562,"PdG","Spinning Block Arena Chest","Pico de Gallo","chest"),
    GuacLocationData(563,"PdG","Void Alux Quest Chest 1","Pico de Gallo","chest"),
    GuacLocationData(564,"PdG","Void Alux Quest Chest 2","Pico de Gallo","chest"),
    GuacLocationData(565,"PdG","Void Alux Quest Chest 3","Pico de Gallo","chest"),
    GuacLocationData(566,"PdG","Lava Filled Passage Chest","Pico de Gallo","chest"),
    GuacLocationData(567,"PdG","Near Sierra Exit Chest","Pico de Gallo","chest"),
    GuacLocationData(568,"PdG","Moving Gear Jump Puzzle Chest","Pico de Gallo","chest"),
    
    # Desierto Caliente 601-650
    GuacLocationData(601, "DC", "Near Tule Tree Chest","Desierto Caliente", "chest"),
    GuacLocationData(602, "DC", "Near Luchita Chest","Desierto Caliente", "chest"),
    GuacLocationData(603, "DC", "Chupacabra Pollo Hole Chest","Desierto Caliente", "chest"),
    GuacLocationData(604, "DC", "Chupacabra Mound Chest","Desierto Caliente", "chest"),
    GuacLocationData(605, "DC", "Dimension Swap Platform Chest","Desierto Caliente", "chest"),
    GuacLocationData(606, "DC", "Under Overhang Chest","Desierto Caliente", "chest"),
    GuacLocationData(607, "DC", "Above Overhang Chest","Desierto Caliente", "chest"),
    GuacLocationData(608, "DC", "Near Temple of War Chest","Desierto Caliente", "chest"),
    GuacLocationData(609, "DC", "Pollo Above Shield Intro Chest","Desierto Caliente", "chest"),
    GuacLocationData(610, "DC", "Central Room Left Chest","Desierto Caliente", "chest"),
    GuacLocationData(611, "DC", "Central Room Right Chest","Desierto Caliente", "chest"),
    GuacLocationData(612, "DC", "Before Pollo Maze Lower Chest","Desierto Caliente", "chest"),
    GuacLocationData(613, "DC", "Before Pollo Maze Upper Chest","Desierto Caliente", "chest"),
    GuacLocationData(614, "DC", "Pollo Below Shield Intro Chest","Desierto Caliente", "chest"),

    # El Infierno 651-750
     GuacLocationData(651,"EI","Silver Room Chest","El Infierno","chest"),
     GuacLocationData(652,"EI","Bronze Room Chest","El Infierno","chest"),
    # GuacLocationData(653, "EI", "Challenge Room #1 Bronze",  El Infierno", "bronze"),
    # GuacLocationData(654, "EI", "Challenge Room #1 Silver",  El Infierno", "silver"),
    # GuacLocationData(655, "EI", "Challenge Room #1 Gold",  El Infierno", "gold"),
    # GuacLocationData(656, "EI", "Challenge Room #2 Bronze",  El Infierno", "bronze"),
    # GuacLocationData(657, "EI", "Challenge Room #2 Silver",  El Infierno", "silver"),
    # GuacLocationData(659, "EI", "Challenge Room #2 Gold",  El Infierno", "gold"),
    # GuacLocationData(660, "EI", "Challenge Room #3 Bronze",  El Infierno", "bronze"),
    # GuacLocationData(661, "EI", "Challenge Room #3 Silver",  El Infierno", "silver"),
    # GuacLocationData(662, "EI", "Challenge Room #3 Gold",  El Infierno", "gold"),
    # GuacLocationData(663, "EI", "Challenge Room #4 Bronze",  El Infierno", "bronze"),
    # GuacLocationData(664, "EI", "Challenge Room #4 Silver",  El Infierno", "silver"),
    # GuacLocationData(665, "EI", "Challenge Room #4 Gold",  El Infierno", "gold"),
    # GuacLocationData(666, "EI", "Challenge Room #5 Bronze",  El Infierno", "bronze"),
    # GuacLocationData(667, "EI", "Challenge Room #5 Silver",  El Infierno", "silver"),
    # GuacLocationData(668, "EI", "Challenge Room #5 Gold",  El Infierno", "gold"),
    # GuacLocationData(669, "EI", "Challenge Room #6 Bronze",  El Infierno", "bronze"),
    # GuacLocationData(670, "EI", "Challenge Room #6 Silver",  El Infierno", "silver"),
    # GuacLocationData(671, "EI", "Challenge Room #6 Gold",  El Infierno", "gold"),
    # GuacLocationData(672, "EI", "Challenge Room #7 Bronze",  El Infierno", "bronze"),
    # GuacLocationData(673, "EI", "Challenge Room #7 Silver",  El Infierno", "silver"),
    # GuacLocationData(674, "EI", "Challenge Room #7 Gold",  El Infierno", "gold"),
    # GuacLocationData(675, "EI", "Challenge Room #8 Bronze",  El Infierno", "bronze"),
    # GuacLocationData(676, "EI", "Challenge Room #8 Silver",  El Infierno", "silver"),
    # GuacLocationData(677, "EI", "Challenge Room #8 Gold",  El Infierno", "gold"),
    # GuacLocationData(678, "EI", "Challenge Room #9 Bronze",  El Infierno", "bronze"),
    # GuacLocationData(679, "EI", "Challenge Room #9 Silver",  El Infierno", "silver"),
    # GuacLocationData(680, "EI", "Challenge Room #9 Gold",  El Infierno", "gold"),
    # GuacLocationData(681, "EI", "Challenge Room #10 Bronze",  El Infierno", "bronze"),
    # GuacLocationData(682, "EI", "Challenge Room #10 Silver",  El Infierno", "silver"),
    # GuacLocationData(683, "EI", "Challenge Room #10 Gold",  El Infierno", "gold"),
    # GuacLocationData(684, "EI", "Challenge Room #11 Bronze",  El Infierno", "bronze"),
    # GuacLocationData(685, "EI", "Challenge Room #11 Silver",  El Infierno", "silver"),
    # GuacLocationData(686, "EI", "Challenge Room #11 Gold",  El Infierno", "gold"),
    # GuacLocationData(687, "EI", "Challenge Room #12 Bronze",  El Infierno", "bronze"),
    # GuacLocationData(688, "EI", "Challenge Room #12 Silver",  El Infierno", "silver"),
    # GuacLocationData(690, "EI", "Challenge Room #12 Gold",  El Infierno", "gold"),
    # GuacLocationData(691, "EI", "Challenge Room #13 Bronze",  El Infierno", "bronze"),
    # GuacLocationData(692, "EI", "Challenge Room #13 Silver",  El Infierno", "silver"),
    # GuacLocationData(693, "EI", "Challenge Room #13 Gold",  El Infierno", "gold"),
    # GuacLocationData(694, "EI", "Challenge Room #14 Bronze",  El Infierno", "bronze"),
    # GuacLocationData(695, "EI", "Challenge Room #14 Silver",  El Infierno", "silver"),
    # GuacLocationData(696, "EI", "Challenge Room #14 Gold",  El Infierno", "gold"),
    # GuacLocationData(697, "EI", "Challenge Room #15 Bronze",  El Infierno", "bronze"),
    # GuacLocationData(698, "EI", "Challenge Room #15 Silver",  El Infierno", "silver"),
    # GuacLocationData(699, "EI", "Challenge Room #15 Gold",  El Infierno", "gold"),
    # GuacLocationData(700, "EI", "Challenge Room #16 Bronze",  El Infierno", "bronze"),
    # GuacLocationData(701, "EI", "Challenge Room #16 Silver",  El Infierno", "silver"),
    # GuacLocationData(702, "EI", "Challenge Room #16 Gold",  El Infierno", "gold"),
    # GuacLocationData(703, "EI", "Challenge Room #17 Bronze",  El Infierno", "bronze"),
    # GuacLocationData(704, "EI", "Challenge Room #17 Silver",  El Infierno", "silver"),
    # GuacLocationData(705, "EI", "Challenge Room #17 Gold",  El Infierno", "gold"),

    # ChacMool Orbs 751-800
    GuacLocationData(751, "ChacMool", "Caverna Orb", "Caverna del Pollo", "orb"),
    GuacLocationData(752, "ChacMool", "Sierra Orb", "Sierra Morena", "orb"),
    GuacLocationData(753, "ChacMool", "Forest del Chivo Orb", "Forest Upper Right", "orb"),
    GuacLocationData(754, "ChacMool", "Tule Tree Orb", "Tule Tree", "orb"),
    GuacLocationData(755, "ChacMool", "Agave Field Orb", "Agave Field", "orb"),
    GuacLocationData(756, "ChacMool", "Infierno Orb", "El Infierno", "orb"),
}