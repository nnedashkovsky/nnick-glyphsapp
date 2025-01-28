#MenuTitle: Round Kerning to Nearest 5
# encoding: utf-8
# by Nick Nedashkovsky

"""
Rounds kerning values to the nearest multiple of 5.
Kerning values smaller than MIN_VALUE are removed.
"""

MIN_VALUE = 5  # Minimum kerning value; values smaller than this will be removed
QUANTISATION = 5  # Step for rounding to the nearest multiple


from GlyphsApp import *
from GlyphsApp import MGOrderedDictionary

font = Glyphs.font

def round_kerning():
    """
    Iterates through the kerning values in the font and:
    - Rounds them to the nearest multiple of QUANTISATION.
    - Removes values with an absolute magnitude smaller than MIN_VALUE.
    """
    kerning = font.kerning  # Access the kerning dictionary
    rounded_pairs_count = 0  # Counter for the number of rounded pairs
    removed_pairs_count = 0  # Counter for the number of removed pairs
    removed_pairs = []  # List to store removed kerning pairs

    for master in font.masters:
        masterDict = kerning[master.id]  # Get kerning values for the current master
        newMasterDict = MGOrderedDictionary.new()  # Initialize a new kerning dictionary for the master
        firstKeys = masterDict.keys()  # Get the left-side glyph IDs (first keys)
        for firstKey in firstKeys:
            rightDict = masterDict[firstKey]  # Get the right-side kerning values (second dictionary)
            secondKeys = rightDict.keys()  # Get the right-side glyph IDs (second keys)
            newRightDict = MGOrderedDictionary.new()  # Initialize a new dictionary for the right-side values
            for secondKey in secondKeys:
                value = rightDict[secondKey]  # Get the kerning value
                # Round the value to the nearest multiple of QUANTISATION
                new_value = round(value / QUANTISATION) * QUANTISATION
                if abs(new_value) >= MIN_VALUE:
                    newRightDict[secondKey] = new_value
                    if value != new_value:  # Count only if the value was actually rounded
                        rounded_pairs_count += 1
                else:
                    # If the value is removed, log the pair
                    removed_pairs_count += 1
                    left_glyph = font.glyphForId_(firstKey)
                    right_glyph = font.glyphForId_(secondKey)
                    removed_pairs.append(f"{left_glyph.name}{right_glyph.name} ({value})")
            # Add the new right-side dictionary if it contains any kerning pairs
            if len(newRightDict) > 0:
                newMasterDict[firstKey] = newRightDict
        # Update the kerning for the current master
        kerning[master.id] = newMasterDict
    font.kerning = kerning  # Apply the updated kerning dictionary to the font

    # Print the results
    print(f"Rounded kerning pairs: {rounded_pairs_count}")
    print(f"Removed kerning pairs: {removed_pairs_count}")
    if removed_pairs:
        print("List of removed kerning pairs:")
        for pair in removed_pairs:
            print(pair)

round_kerning()
