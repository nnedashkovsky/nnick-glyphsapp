# nnick-glyphsapp

scripts to be used in glyphs3 app




# Round Kerning to Nearest 5
This script rounds the kerning values in a font to the nearest multiple of 5. It also removes any kerning values that are smaller than a minimum threshold, defined by MIN_VALUE.

**Features:**
Rounds kerning values: Kerning values are rounded to the nearest multiple of 5 (modifiable through QUANTISATION).
Removes small kerning values: Values smaller than MIN_VALUE are removed from the kerning dictionary.
Displays a summary: After running, the script prints a summary with the number of rounded and removed kerning pairs.
**Parameters:**
MIN_VALUE: Minimum kerning value. Any kerning value smaller than this will be removed. Default is 5.
QUANTISATION: The step for rounding kerning values to the nearest multiple. Default is 5.
