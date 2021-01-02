"""
file: positronium_spectrum.py
brief:
author: S. V. Paulauskas
date: January 02, 2021
"""

spectrum = [1, 2, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 3, 0, 0, 0, 4, 0, 1,
            0, 2, 2, 2, 1, 2, 1, 1, 0, 0, 0, 0, 1, 1, 0, 2, 1, 1, 1, 1, 1, 0, 1, 0, 2, 0, 0, 2, 0,
            0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 4, 2, 3, 0, 2, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 2,
            1, 2, 1, 0, 1, 2, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 2, 2, 1, 1,
            2, 0, 0, 0, 0, 0, 0, 1, 2, 0, 1, 1, 1, 1, 0, 2, 1, 0, 0, 0, 1, 0, 0, 1, 0, 2, 0, 1, 0,
            0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 2, 1, 0, 1, 0,
            2, 1, 0, 1, 3, 1, 0, 0, 0, 1, 1, 2, 2, 0, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2,
            1, 0, 0, 1, 1, 2, 0, 2, 2, 4, 1, 2, 2, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1,
            0, 0, 1, 5, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 2, 0, 2, 0, 0, 0, 0, 1, 0, 1, 1, 2, 0, 1,
            3, 1, 1, 2, 2, 1, 0, 2, 0, 2, 4, 1, 0, 0, 1, 0, 0, 0, 0, 0, 2, 1, 1, 0, 0, 0, 2, 2, 0,
            0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 2, 3, 0, 0, 0, 1, 1, 0, 2, 1, 1, 0, 1, 0, 0, 2,
            1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 2, 1, 1, 1, 0, 1, 1, 0, 2, 1, 0, 2, 1,
            1, 1, 1, 3, 0, 0, 1, 2, 0, 1, 2, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 2, 0, 0,
            1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 4, 0, 1, 0, 2, 1, 0, 1, 0, 1, 2, 0,
            1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 2, 0, 0, 0, 1,
            2, 0, 0, 2, 1, 2, 3, 3, 0, 1, 1, 1, 0, 5, 1, 2, 0, 0, 2, 0, 0, 2, 0, 1, 0, 1, 0, 0, 0,
            1, 2, 1, 2, 1, 2, 1, 0, 1, 0, 2, 1, 1, 0, 1, 1, 0, 2, 2, 0, 1, 1, 0, 1, 0, 1, 2, 2, 2,
            1, 2, 1, 2, 2, 1, 2, 2, 1, 2, 0, 0, 1, 0, 1, 1, 0, 2, 1, 2, 0, 0, 0, 4, 1, 2, 0, 0, 1,
            1, 1, 0, 1, 0, 1, 2, 0, 1, 0, 2, 1, 2, 0, 1, 1, 0, 0, 3, 2, 1, 0, 1, 0, 1, 3, 2, 1, 0,
            0, 0, 0, 0, 2, 1, 0, 2, 1, 1, 1, 1, 1, 1, 2, 1, 0, 1, 0, 2, 2, 1, 1, 2, 1, 0, 1, 1, 4,
            0, 2, 2, 3, 1, 0, 4, 3, 4, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 3, 0, 0, 1, 0, 1, 0, 0, 1, 1,
            1, 2, 2, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 2, 0, 2, 0, 1, 0, 0, 3, 1, 2, 4, 2, 2, 1,
            1, 0, 2, 1, 0, 1, 1, 1, 1, 0, 2, 2, 1, 1, 2, 3, 0, 1, 2, 2, 0, 2, 1, 2, 2, 1, 1, 0, 0,
            3, 1, 0, 2, 0, 0, 0, 2, 1, 0, 1, 2, 1, 1, 0, 1, 2, 0, 2, 1, 0, 2, 0, 1, 2, 0, 1, 0, 1,
            2, 1, 0, 2, 3, 1, 0, 3, 3, 0, 1, 0, 4, 1, 1, 0, 0, 0, 1, 0, 1, 1, 2, 0, 4, 2, 2, 0, 1,
            3, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 2, 0, 1, 1, 3, 2, 1, 2, 0, 1, 1, 2, 0, 1, 1, 0,
            1, 5, 3, 1, 3, 0, 1, 2, 1, 1, 1, 2, 0, 1, 0, 0, 0, 2, 2, 1, 0, 2, 2, 1, 0, 1, 0, 2, 1,
            1, 0, 0, 0, 2, 3, 2, 0, 0, 4, 3, 0, 0, 2, 3, 0, 2, 3, 4, 1, 0, 0, 1, 1, 3, 2, 0, 0, 2,
            2, 0, 2, 2, 1, 1, 3, 0, 1, 1, 1, 2, 2, 0, 1, 0, 1, 0, 0, 2, 2, 0, 1, 2, 2, 1, 0, 2, 1,
            1, 1, 1, 0, 2, 0, 2, 1, 1, 1, 0, 1, 4, 3, 0, 2, 1, 3, 2, 0, 1, 0, 0, 2, 0, 0, 0, 3, 4,
            2, 1, 2, 0, 2, 1, 2, 1, 1, 2, 1, 2, 0, 2, 1, 3, 0, 1, 2, 0, 2, 0, 0, 2, 1, 0, 1, 1, 0,
            2, 3, 1, 4, 1, 1, 2, 3, 2, 0, 1, 0, 4, 0, 1, 1, 0, 1, 0, 1, 2, 0, 0, 2, 1, 2, 4, 2, 0,
            1, 2, 3, 2, 1, 0, 1, 1, 0, 1, 3, 0, 0, 4, 0, 2, 2, 0, 1, 2, 0, 2, 1, 0, 1, 2, 1, 1, 1,
            2, 3, 1, 4, 1, 0, 2, 1, 1, 1, 2, 1, 0, 1, 2, 2, 2, 1, 1, 1, 3, 2, 0, 2, 0, 1, 1, 2, 1,
            1, 2, 1, 0, 1, 1, 2, 2, 2, 3, 1, 4, 3, 1, 3, 1, 2, 2, 1, 2, 1, 1, 0, 0, 3, 1, 0, 2, 0,
            1, 3, 0, 3, 0, 2, 1, 5, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 2, 0, 0, 0, 2, 1, 2, 1, 0, 3, 1,
            3, 1, 1, 3, 0, 4, 0, 2, 1, 0, 3, 2, 0, 2, 0, 1, 1, 3, 1, 1, 1, 2, 2, 1, 3, 1, 3, 3, 0,
            1, 0, 2, 0, 2, 1, 0, 2, 1, 0, 1, 0, 1, 2, 3, 0, 1, 0, 1, 0, 3, 1, 1, 0, 5, 3, 0, 1, 0,
            0, 1, 1, 1, 1, 1, 1, 0, 3, 1, 2, 3, 2, 1, 3, 1, 1, 1, 0, 0, 1, 0, 2, 0, 2, 3, 0, 1, 2,
            3, 0, 1, 0, 0, 1, 2, 1, 1, 2, 2, 1, 1, 2, 0, 1, 0, 1, 1, 1, 1, 3, 1, 1, 1, 1, 3, 1, 2,
            1, 3, 2, 0, 0, 0, 4, 6, 1, 2, 2, 0, 2, 2, 2, 2, 0, 4, 0, 3, 3, 1, 0, 0, 0, 1, 1, 3, 0,
            0, 1, 1, 1, 1, 0, 1, 2, 5, 1, 0, 3, 1, 0, 1, 2, 1, 3, 0, 1, 0, 2, 1, 0, 2, 0, 1, 1, 2,
            1, 0, 1, 0, 1, 0, 3, 1, 0, 0, 1, 3, 1, 2, 3, 1, 0, 2, 1, 2, 0, 3, 0, 1, 1, 2, 5, 0, 1,
            1, 2, 1, 0, 1, 1, 2, 2, 2, 3, 1, 1, 3, 1, 1, 1, 2, 3, 2, 2, 4, 0, 1, 1, 2, 3, 2, 2, 2,
            1, 3, 2, 2, 3, 0, 3, 1, 3, 3, 2, 2, 0, 2, 3, 0, 2, 4, 1, 2, 3, 2, 5, 0, 3, 0, 0, 1, 1,
            2, 0, 1, 1, 2, 1, 3, 1, 1, 1, 3, 1, 2, 5, 1, 2, 1, 1, 4, 2, 2, 0, 3, 0, 2, 2, 3, 1, 0,
            1, 1, 1, 3, 1, 1, 4, 0, 3, 2, 1, 0, 4, 2, 0, 2, 1, 1, 0, 2, 1, 4, 0, 1, 0, 3, 2, 1, 1,
            3, 2, 1, 2, 2, 0, 0, 2, 1, 2, 3, 1, 0, 2, 3, 0, 3, 1, 1, 0, 2, 3, 2, 3, 1, 0, 3, 1, 0,
            1, 2, 1, 0, 1, 2, 1, 1, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 2, 1, 3, 1, 2, 3, 2, 1, 1, 2, 4,
            1, 1, 4, 0, 2, 1, 1, 1, 1, 5, 2, 1, 2, 2, 2, 1, 1, 0, 2, 2, 1, 1, 0, 1, 1, 4, 2, 1, 2,
            3, 2, 1, 3, 5, 2, 1, 3, 3, 0, 2, 0, 4, 1, 0, 3, 1, 2, 3, 0, 3, 2, 2, 4, 2, 3, 4, 0, 3,
            2, 3, 3, 2, 0, 0, 2, 1, 3, 1, 2, 3, 0, 2, 0, 2, 2, 1, 3, 1, 1, 3, 1, 3, 2, 2, 3, 1, 2,
            2, 3, 2, 0, 1, 1, 1, 2, 0, 2, 2, 3, 2, 2, 4, 4, 2, 0, 2, 2, 4, 1, 1, 3, 3, 2, 3, 0, 3,
            1, 2, 1, 3, 0, 0, 2, 3, 2, 2, 2, 4, 4, 2, 0, 0, 0, 3, 2, 4, 1, 0, 1, 1, 1, 1, 0, 3, 3,
            5, 0, 2, 2, 2, 0, 3, 0, 2, 2, 2, 0, 2, 3, 3, 4, 1, 1, 4, 0, 2, 0, 1, 1, 2, 1, 3, 3, 1,
            3, 0, 4, 0, 1, 3, 4, 0, 3, 0, 2, 1, 2, 3, 1, 3, 0, 4, 1, 0, 1, 4, 2, 3, 1, 1, 1, 2, 0,
            2, 3, 1, 4, 2, 3, 1, 0, 7, 1, 2, 2, 3, 1, 4, 3, 2, 0, 1, 1, 2, 2, 3, 1, 1, 4, 0, 0, 3,
            1, 3, 2, 3, 3, 2, 1, 3, 2, 1, 1, 1, 2, 1, 3, 3, 3, 0, 1, 3, 1, 0, 4, 3, 0, 0, 2, 2, 3,
            1, 2, 2, 2, 1, 0, 0, 3, 4, 0, 0, 2, 2, 5, 4, 3, 1, 0, 1, 3, 3, 1, 4, 2, 5, 4, 2, 5, 0,
            1, 2, 1, 4, 4, 5, 3, 4, 2, 1, 5, 0, 1, 3, 2, 1, 3, 2, 2, 2, 2, 1, 1, 3, 1, 1, 2, 5, 1,
            3, 1, 2, 3, 2, 2, 2, 5, 1, 1, 2, 3, 3, 2, 3, 7, 2, 1, 7, 1, 5, 3, 5, 3, 3, 2, 3, 4, 3,
            1, 4, 2, 1, 1, 2, 2, 2, 3, 2, 2, 1, 3, 3, 3, 1, 5, 2, 2, 0, 1, 9, 5, 4, 4, 2, 4, 1, 3,
            3, 1, 3, 1, 3, 0, 1, 3, 4, 3, 2, 4, 1, 3, 0, 1, 2, 1, 5, 8, 3, 0, 1, 6, 3, 0, 1, 3, 4,
            5, 0, 8, 4, 4, 3, 5, 5, 4, 7, 3, 2, 5, 3, 4, 2, 3, 1, 2, 3, 2, 0, 1, 1, 6, 4, 3, 4, 3,
            0, 5, 3, 2, 1, 7, 2, 7, 2, 2, 0, 1, 3, 5, 1, 2, 5, 0, 8, 2, 2, 5, 3, 2, 7, 3, 4, 2, 5,
            4, 1, 0, 6, 5, 6, 0, 5, 2, 6, 3, 4, 6, 10, 3, 2, 1, 3, 5, 6, 6, 2, 2, 1, 8, 1, 4, 1, 1,
            2, 2, 5, 5, 3, 3, 6, 6, 4, 4, 2, 4, 3, 9, 4, 4, 3, 1, 3, 3, 7, 1, 3, 5, 5, 1, 3, 2, 1,
            4, 4, 4, 1, 5, 5, 2, 2, 7, 7, 3, 4, 7, 4, 6, 15, 6, 6, 5, 5, 3, 4, 3, 8, 3, 3, 4, 3, 4,
            5, 4, 1, 3, 3, 6, 7, 3, 3, 5, 5, 5, 3, 4, 4, 4, 3, 4, 5, 5, 3, 3, 3, 4, 4, 1, 3, 2, 5,
            2, 2, 4, 8, 5, 6, 3, 6, 4, 4, 8, 5, 5, 2, 7, 10, 5, 6, 3, 6, 5, 10, 9, 2, 6, 7, 11, 8,
            9, 5, 6, 6, 12, 8, 4, 6, 6, 5, 8, 3, 7, 10, 6, 4, 8, 6, 8, 8, 5, 4, 11, 8, 4, 4, 8, 8,
            4, 11, 5, 9, 8, 7, 12, 8, 8, 7, 5, 5, 6, 9, 8, 8, 8, 9, 10, 10, 10, 10, 7, 1, 9, 9, 8,
            11, 8, 11, 7, 13, 13, 9, 10, 10, 5, 6, 6, 6, 8, 11, 9, 10, 11, 11, 10, 9, 10, 12, 9, 5,
            9, 11, 18, 9, 9, 9, 9, 9, 14, 9, 9, 13, 11, 7, 14, 8, 8, 7, 13, 14, 15, 13, 8, 12, 9,
            13, 10, 7, 11, 11, 12, 17, 14, 8, 13, 13, 11, 20, 11, 14, 13, 19, 9, 14, 14, 14, 16, 15,
            14, 11, 19, 19, 9, 25, 22, 14, 16, 9, 11, 15, 17, 15, 15, 14, 18, 11, 15, 21, 11, 16,
            17, 20, 21, 18, 18, 12, 15, 17, 24, 15, 21, 13, 17, 20, 23, 20, 24, 23, 21, 23, 19, 23,
            29, 16, 23, 13, 22, 25, 22, 29, 36, 32, 15, 29, 25, 32, 28, 33, 22, 24, 38, 21, 41, 31,
            25, 28, 33, 35, 30, 27, 22, 45, 31, 27, 35, 36, 29, 42, 25, 43, 40, 41, 38, 48, 42, 46,
            35, 28, 50, 40, 37, 36, 37, 33, 40, 40, 45, 41, 44, 49, 42, 49, 37, 51, 49, 50, 56, 55,
            53, 32, 72, 53, 58, 68, 60, 55, 47, 54, 69, 65, 62, 63, 56, 81, 67, 66, 68, 59, 66, 68,
            72, 78, 72, 73, 67, 80, 91, 69, 83, 75, 82, 92, 76, 89, 90, 87, 91, 87, 75, 83, 89, 94,
            87, 72, 92, 86, 90, 93, 102, 94, 104, 104, 94, 108, 108, 85, 123, 116, 105, 113, 101,
            115, 111, 109, 121, 126, 135, 116, 143, 111, 123, 112, 141, 125, 156, 117, 149, 136,
            134, 146, 135, 129, 141, 135, 149, 165, 142, 142, 150, 153, 143, 150, 135, 174, 151,
            194, 157, 167, 193, 170, 183, 182, 189, 170, 191, 143, 174, 174, 171, 174, 192, 202,
            189, 193, 199, 216, 207, 201, 193, 242, 230, 197, 241, 203, 253, 272, 203, 234, 229,
            240, 238, 252, 255, 243, 266, 257, 250, 244, 243, 248, 262, 269, 268, 255, 269, 274,
            247, 312, 277, 309, 288, 298, 306, 278, 278, 276, 321, 298, 278, 313, 305, 313, 316,
            309, 285, 351, 289, 329, 288, 304, 282, 326, 298, 344, 321, 336, 356, 293, 330, 323,
            346, 352, 371, 370, 380, 389, 353, 354, 379, 352, 345, 370, 346, 370, 346, 362, 381,
            380, 388, 400, 363, 365, 381, 413, 336, 372, 397, 391, 380, 417, 395, 406, 370, 411,
            398, 390, 370, 381, 364, 408, 401, 386, 383, 403, 422, 380, 384, 398, 412, 389, 401,
            364, 391, 403, 396, 366, 370, 396, 393, 371, 391, 352, 413, 444, 385, 397, 408, 410,
            383, 431, 433, 375, 389, 417, 417, 415, 357, 431, 423, 394, 411, 400, 395, 374, 401,
            404, 420, 412, 434, 373, 399, 418, 410, 411, 373, 382, 364, 385, 350, 369, 383, 394,
            406, 339, 366, 362, 357, 355, 402, 363, 389, 356, 362, 336, 381, 365, 351, 332, 348,
            334, 360, 362, 360, 359, 354, 357, 360, 348, 325, 362, 347, 314, 334, 315, 327, 320,
            325, 339, 299, 340, 313, 307, 337, 305, 303, 307, 298, 316, 298, 344, 271, 299, 347,
            313, 305, 308, 291, 286, 278, 313, 298, 243, 303, 262, 277, 272, 266, 255, 288, 274,
            272, 254, 276, 257, 287, 252, 258, 266, 263, 259, 254, 232, 249, 235, 254, 230, 262,
            218, 217, 222, 220, 234, 258, 251, 252, 221, 230, 234, 244, 244, 178, 231, 208, 220,
            229, 213, 214, 225, 243, 197, 201, 228, 216, 189, 202, 203, 212, 193, 197, 188, 202,
            189, 199, 179, 186, 162, 167, 179, 179, 163, 177, 168, 178, 158, 159, 171, 181, 153,
            162, 196, 163, 157, 170, 157, 164, 169, 165, 153, 174, 148, 150, 146, 138, 159, 167,
            164, 146, 150, 177, 151, 140, 154, 148, 137, 139, 140, 137, 144, 120, 155, 143, 115,
            147, 132, 131, 124, 146, 116, 114, 149, 123, 130, 108, 120, 127, 117, 126, 106, 129,
            116, 109, 96, 102, 99, 114, 109, 106, 104, 97, 110, 103, 111, 92, 93, 96, 101, 91, 118,
            107, 108, 110, 99, 98, 87, 99, 96, 89, 97, 110, 99, 101, 93, 91, 78, 89, 89, 83, 94,
            101, 92, 91, 90, 96, 91, 67, 67, 88, 97, 94, 84, 84, 84, 85, 68, 80, 81, 78, 76, 94, 65,
            64, 85, 78, 90, 68, 79, 82, 74, 75, 81, 74, 89, 70, 66, 67, 92, 75, 66, 71, 66, 79, 63,
            81, 60, 57, 62, 54, 68, 59, 58, 66, 70, 72, 60, 74, 74, 63, 60, 60, 51, 69, 73, 65, 65,
            76, 60, 69, 67, 57, 73, 58, 63, 52, 63, 66, 60, 61, 70, 40, 47, 69, 67, 69, 52, 52, 70,
            62, 56, 59, 68, 54, 43, 64, 54, 65, 63, 44, 54, 39, 48, 58, 66, 39, 62, 55, 48, 54, 51,
            46, 47, 37, 42, 59, 57, 46, 46, 48, 49, 43, 43, 47, 46, 50, 48, 55, 45, 36, 45, 55, 65,
            48, 42, 66, 49, 34, 51, 31, 46, 47, 46, 50, 48, 46, 54, 44, 33, 53, 33, 37, 38, 50, 40,
            37, 40, 31, 35, 40, 50, 33, 39, 48, 46, 45, 46, 36, 46, 34, 34, 47, 43, 47, 43, 34, 44,
            45, 56, 38, 48, 34, 37, 44, 42, 40, 38, 45, 31, 48, 38, 32, 38, 27, 43, 37, 40, 34, 34,
            36, 34, 39, 50, 39, 41, 43, 35, 31, 31, 38, 43, 30, 41, 30, 32, 30, 37, 33, 43, 30, 36,
            37, 24, 45, 36, 29, 26, 36, 34, 42, 34, 30, 46, 31, 34, 33, 36, 25, 28, 25, 30, 28, 24,
            34, 27, 23, 25, 27, 35, 28, 26, 34, 31, 42, 29, 33, 31, 31, 23, 34, 24, 26, 28, 31, 30,
            25, 28, 31, 36, 35, 30, 35, 38, 36, 27, 45, 26, 24, 26, 28, 26, 40, 39, 37, 30, 23, 27,
            30, 39, 32, 26, 30, 27, 36, 30, 35, 30, 25, 37, 33, 25, 26, 24, 35, 29, 27, 24, 22, 26,
            31, 33, 28, 30, 26, 26, 30, 28, 23, 37, 28, 32, 33, 25, 22, 26, 26, 26, 25, 37, 18, 26,
            25, 28, 37, 24, 29, 26, 23, 33, 21, 26, 28, 21, 16, 25, 26, 27, 33, 25, 31, 42, 28, 27,
            21, 19, 40, 17, 28, 28, 24, 21, 23, 24, 30, 19, 38, 27, 20, 17, 29, 29, 29, 27, 31, 37,
            29, 30, 34, 25, 19, 19, 37, 28, 23, 17, 24, 14, 25, 31, 27, 23, 23, 28, 20, 26, 29, 31,
            22, 17, 29, 22, 24, 21, 19, 18, 25, 24, 34, 21, 22, 30, 23, 22, 29, 31, 28, 25, 21, 17,
            33, 24, 37, 23, 25, 24, 21, 24, 16, 35, 32, 33, 28, 27, 22, 28, 20, 30, 26, 17, 17, 33,
            20, 23, 18, 24, 24, 21, 29, 27, 24, 20, 16, 26, 25, 24, 26, 23, 21, 24, 25, 22, 21, 26,
            27, 18, 23, 26, 22, 28, 22, 16, 20, 18, 21, 26, 15, 16, 22, 14, 18, 27, 21, 16, 16, 28,
            19, 25, 18, 17, 26, 23, 19, 21, 25, 21, 24, 19, 33, 24, 19, 21, 24, 25, 22, 13, 21, 12,
            20, 24, 21, 22, 19, 18, 18, 17, 14, 20, 20, 21, 14, 21, 25, 13, 16, 21, 21, 28, 15, 21,
            17, 16, 25, 20, 16, 18, 19, 19, 21, 25, 23, 19, 21, 25, 21, 26, 15, 13, 24, 27, 11, 16,
            9, 20, 29, 26, 14, 20, 20, 16, 17, 22, 16, 22, 21, 14, 23, 16, 15, 24, 25, 9, 17, 14,
            15, 17, 13, 19, 9, 29, 18, 27, 17, 15, 15, 19, 9, 16, 17, 17, 18, 19, 17, 14, 14, 11,
            17, 18, 21, 13, 24, 22, 17, 9, 19, 11, 12, 19, 19, 10, 24, 25, 18, 11, 11, 14, 16, 19,
            18, 11, 20, 19, 18, 14, 13, 26, 20, 10, 26, 15, 24, 15, 22, 14, 17, 17, 17, 11, 14, 22,
            14, 23, 15, 19, 20, 19, 20, 14, 14, 17, 16, 21, 15, 22, 23, 15, 19, 15, 19, 25, 11, 12,
            9, 16, 17, 18, 21, 11, 19, 22, 23, 21, 21, 12, 16, 24, 13, 21, 17, 14, 8, 15, 17, 14,
            16, 16, 20, 10, 16, 16, 12, 18, 17, 15, 22, 15, 15, 21, 18, 15, 4, 8, 15, 16, 16, 16,
            19, 22, 14, 14, 9, 16, 22, 14, 18, 12, 8, 16, 14, 13, 10, 12, 16, 12, 15, 7, 16, 21, 12,
            13, 16, 16, 13, 15, 9, 14, 14, 16, 17, 20, 16, 11, 18, 10, 18, 10, 12, 18, 14, 9, 15,
            18, 13, 17, 18, 10, 9, 19, 12, 12, 9, 8, 13, 10, 15, 15, 15, 10, 14, 11, 20, 9, 12, 17,
            14, 15, 12, 8, 16, 19, 11, 15, 14, 16, 15, 20, 7, 14, 18, 8, 8, 18, 10, 14, 15, 10, 10,
            9, 12, 9, 9, 10, 9, 19, 13, 12, 19, 16, 7, 14, 19, 9, 13, 10, 9, 14, 9, 20, 13, 9, 12,
            7, 13, 14, 13, 11, 12, 9, 12, 12, 13, 14, 17, 8, 10, 13, 15, 16, 7, 9, 11, 9, 12, 12,
            11, 12, 16, 13, 9, 12, 10, 12, 11, 16, 8, 10, 12, 12, 11, 10, 7, 6, 9, 5, 14, 17, 10, 8,
            6, 15, 10, 11, 12, 13, 11, 14, 10, 13, 10, 11, 16, 8, 10, 8, 11, 12, 7, 9, 16, 11, 8,
            13, 9, 11, 18, 6, 10, 13, 10, 10, 13, 10, 12, 10, 9, 11, 12, 8, 8, 11, 14, 9, 13, 13, 7,
            10, 8, 11, 7, 12, 10, 10, 15, 14, 13, 14, 10, 8, 16, 14, 5, 8, 6, 10, 13, 7, 11, 12, 8,
            6, 10, 17, 8, 14, 13, 6, 11, 6, 5, 4, 12, 13, 17, 14, 11, 13, 7, 14, 11, 9, 11, 8, 7,
            10, 11, 18, 12, 11, 7, 11, 8, 17, 10, 8, 6, 15, 8, 16, 9, 9, 11, 8, 7, 14, 14, 10, 13,
            9, 8, 9, 12, 7, 12, 9, 4, 9, 14, 12, 2, 9, 4, 16, 8, 5, 11, 11, 8, 10, 7, 11, 9, 13, 7,
            5, 13, 12, 18, 11, 10, 8, 17, 15, 9, 13, 9, 9, 9, 11, 11, 11, 12, 10, 11, 12, 10, 7, 14,
            5, 9, 7, 12, 11, 9, 5, 4, 10, 9, 6, 12, 6, 10, 7, 11, 8, 11, 16, 5, 7, 7, 10, 5, 11, 16,
            11, 12, 10, 10, 6, 5, 8, 9, 11, 12, 9, 12, 9, 10, 4, 7, 9, 12, 9, 5, 5, 4, 8, 15, 7, 7,
            9, 9, 5, 4, 16, 11, 11, 11, 11, 12, 14, 7, 10, 13, 10, 10, 8, 8, 5, 7, 7, 6, 9, 6, 8, 6,
            12, 13, 10, 11, 11, 5, 10, 6, 9, 8, 8, 10, 8, 5, 10, 7, 8, 13, 10, 8, 7, 7, 10, 10, 10,
            8, 3, 14, 7, 15, 7, 8, 7, 12, 14, 7, 11, 9, 4, 17, 2, 11, 9, 12, 7, 7, 12, 10, 9, 5, 7,
            6, 4, 5, 11, 10, 12, 4, 4, 12, 3, 15, 6, 7, 8, 7, 8, 10, 10, 8, 6, 10, 7, 7, 7, 6, 10,
            3, 8, 9, 6, 12, 5, 13, 14, 11, 7, 13, 5, 7, 6, 5, 5, 7, 10, 9, 6, 11, 8, 3, 6, 7, 2, 6,
            7, 7, 11, 7, 11, 6, 6, 11, 7, 12, 7, 8, 5, 10, 5, 6, 6, 9, 3, 9, 5, 8, 12, 6, 4, 9, 13,
            5, 5, 5, 10, 9, 8, 5, 4, 8, 5, 9, 13, 4, 6, 5, 9, 14, 6, 13, 7, 5, 3, 4, 3, 6, 9, 2, 8,
            4, 5, 3, 4, 9, 10, 6, 6, 6, 6, 3, 7, 7, 7, 10, 3, 10, 5, 5, 5, 11, 8, 5, 6, 4, 8, 3, 4,
            4, 8, 5, 5, 5, 6, 7, 5, 5, 5, 10, 10, 6, 5, 10, 2, 6, 7, 7, 1, 11, 10, 8, 2, 8, 7, 4, 5,
            7, 2, 4, 7, 12, 8, 7, 2, 10, 8, 3, 6, 3, 5, 9, 9, 9, 3, 5, 7, 4, 5, 3, 7, 4, 11, 5, 5,
            7, 4, 2, 7, 1, 5, 6, 8, 7, 8, 7, 7, 5, 7, 6, 5, 7, 6, 5, 4, 6, 5, 8, 8, 6, 8, 2, 4, 6,
            6, 6, 6, 2, 3, 4, 9, 2, 7, 6, 6, 8, 4, 8, 3, 3, 1, 7, 6, 5, 1, 2, 9, 9, 8, 3, 4, 6, 3,
            6, 4, 5, 5, 8, 4, 5, 8, 6, 6, 7, 4, 7, 6, 6, 8, 3, 5, 3, 4, 3, 4, 2, 3, 6, 4, 8, 6, 5,
            2, 9, 4, 2, 4, 4, 4, 2, 3, 4, 3, 6, 4, 7, 9, 5, 7, 9, 3, 6, 4, 10, 8, 8, 3, 4, 6, 2, 6,
            5, 8, 6, 5, 4, 5, 3, 5, 5, 3, 2, 6, 4, 8, 6, 4, 5, 8, 7, 3, 7, 3, 6, 4, 6, 5, 6, 2, 8,
            4, 3, 7, 2, 5, 4, 4, 2, 4, 5, 4, 3, 7, 2, 3, 7, 6, 4, 3, 7, 8, 6, 5, 5, 4, 6, 5, 8, 4,
            0, 10, 5, 4, 4, 0, 2, 2, 7, 2, 2, 5, 8, 1, 3, 4, 2, 6, 2, 0, 3, 2, 2, 7, 1, 5, 3, 5, 3,
            5, 3, 4, 4, 6, 3, 4, 1, 4, 8, 3, 2, 5, 3, 2, 3, 8, 8, 4, 3, 5, 1, 3, 2, 2, 2, 3, 5, 9,
            7, 5, 3, 5, 3, 3, 4, 3, 5, 4, 1, 7, 3, 3, 5, 5, 3, 6, 4, 4, 2, 4, 3, 6, 5, 4, 7, 8, 7,
            6, 4, 3, 2, 3, 2, 3, 5, 5, 6, 4, 4, 6, 5, 2, 3, 1, 8, 3, 4, 4, 8, 6, 11, 4, 2, 4, 6, 1,
            1, 0, 2, 4, 3, 6, 0, 3, 3, 6, 5, 0, 5, 2, 2, 3, 4, 8, 6, 4, 5, 6, 2, 3, 3, 3, 5, 4, 4,
            4, 0, 4, 0, 3, 2, 5, 5, 5, 6, 0, 2, 3, 9, 4, 2, 3, 5, 2, 4, 3, 0, 4, 2, 3, 1, 1, 2, 4,
            3, 2, 6, 3, 0, 2, 3, 5, 0, 6, 6, 4, 3, 2, 5, 1, 2, 1, 1, 3, 5, 0, 3, 1, 3, 6, 4, 4, 3,
            3, 1, 7, 0, 2, 5, 5, 1, 5, 1, 4, 1, 5, 2, 3, 3, 1, 4, 5, 3, 4, 2, 2, 4, 5, 4, 6, 2, 3,
            8, 5, 6, 4, 2, 3, 6, 2, 4, 0, 5, 1, 4, 0, 2, 4, 4, 2, 2, 2, 1, 3, 1, 3, 1, 5, 2, 5, 2,
            5, 3, 2, 2, 6, 1, 3, 2, 2, 2, 2, 5, 0, 3, 3, 3, 3, 5, 3, 6, 4, 1, 2, 3, 5, 2, 1, 2, 5,
            4, 2, 5, 1, 3, 1, 6, 3, 1, 4, 2, 2, 1, 3, 1, 7, 4, 4, 5, 5, 5, 3, 4, 4, 4, 4, 3, 3, 2,
            1, 2, 4, 2, 3, 0, 4, 1, 3, 3, 4, 2, 2, 8, 8, 6, 5, 1, 1, 4, 3, 3, 0, 2, 2, 6, 3, 2, 6,
            0, 3, 5, 1, 3, 1, 3, 2, 3, 4, 3, 3, 1, 2, 4, 5, 2, 3, 5, 3, 1, 1, 3, 3, 2, 2, 3, 3, 2,
            0, 4, 1, 3, 1, 5, 0, 3, 1, 6, 3, 1, 4, 4, 1, 5, 2, 4, 1, 4, 2, 3, 3, 1, 5, 1, 5, 1, 4,
            4, 2, 1, 1, 3, 2, 3, 5, 5, 2, 0, 2, 5, 0, 0, 5, 1, 1, 5, 4, 2, 0, 1, 1, 5, 3, 0, 3, 1,
            5, 5, 2, 3, 4, 3, 5, 3, 3, 5, 4, 1, 2, 2, 3, 5, 3, 1, 3, 5, 1, 4, 4, 1, 3, 0, 2, 3, 1,
            2, 2, 5, 2, 2, 3, 5, 6, 1, 1, 3, 2, 2, 4, 2, 2, 5, 1, 2, 1, 1, 4, 1, 4, 1, 2, 2, 3, 3,
            2, 4, 1, 3, 1, 1, 1, 2, 3, 4, 1, 3, 2, 2, 2, 2, 2, 4, 1, 4, 3, 1, 5, 1, 1, 0, 3, 1, 1,
            4, 2, 3, 2, 0, 2, 3, 2, 1, 3, 2, 4, 2, 4, 5, 1, 1, 2, 5, 4, 1, 3, 2, 3, 1, 3, 4, 1, 6,
            2, 1, 4, 6, 1, 1, 4, 2, 1, 3, 3, 1, 8, 1, 2, 4, 3, 2, 4, 1, 5, 1, 0, 3, 2, 2, 0, 6, 0,
            3, 1, 4, 5, 1, 2, 0, 3, 4, 0, 5, 1, 4, 0, 2, 3, 3, 4, 1, 2, 6, 4, 3, 3, 3, 2, 0, 3, 2,
            1, 0, 3, 5, 2, 0, 5, 0, 4, 6, 3, 3, 1, 1, 2, 3, 4, 2, 1, 3, 5, 0, 0, 1, 5, 0, 3, 0, 6,
            1, 1, 0, 2, 1, 3, 3, 2, 3, 2, 4, 1, 0, 1, 1, 2, 1, 1, 1, 2, 1, 3, 3, 2, 2, 3, 3, 1, 3,
            2, 2, 4, 1, 0, 2, 2, 3, 4, 3, 3, 2, 2, 3, 1, 0, 1, 2, 1, 3, 0, 4, 3, 0, 1, 1, 1, 1, 2,
            3, 1, 4, 1, 4, 2, 4, 2, 1, 3, 0, 2, 2, 3, 1, 1, 1, 4, 1, 4, 1, 2, 1, 1, 1, 3, 1, 1, 5,
            2, 1, 3, 3, 3, 1, 0, 3, 2, 0, 1, 1, 1, 0, 3, 3, 1, 1, 1, 0, 0, 2, 2, 0, 2, 1, 2, 1, 3,
            1, 3, 1, 0, 2, 0, 0, 2, 1, 5, 2, 2, 2, 2, 0, 0, 3, 3, 3, 3, 3, 2, 2, 2, 2, 0, 1, 1, 1,
            3, 0, 1, 1, 0, 2, 1, 2, 3, 4, 3, 2, 2, 1, 3, 2, 1, 2, 2, 2, 1, 2, 0, 0, 2, 3, 1, 4, 1,
            6, 0, 5, 4, 2, 2, 5, 1, 4, 3, 4, 2, 2, 1, 1, 4, 3, 4, 1, 2, 3, 1, 1, 2, 0, 2, 1, 2, 3,
            1, 4, 1, 3, 2, 3, 2, 2, 1, 1, 1, 1, 2, 2, 2, 3, 2, 1, 2, 1, 3, 3, 4, 1, 1, 2, 1, 0, 1,
            3, 2, 1, 1, 0, 4, 3, 1, 5, 2, 1, 2, 1, 2, 3, 0, 0, 1, 2, 0, 1, 2, 4, 1, 0, 4, 2, 4, 3,
            1, 3, 0, 2, 3, 2, 3, 1, 1, 1, 2, 2, 2, 2, 0, 4, 1, 0, 2, 2, 1, 2, 2, 1, 1, 2, 4, 1, 1,
            2, 0, 3, 0, 1, 2, 0, 0, 1, 0, 2, 1, 1, 2, 2, 2, 3, 1, 2, 1, 0, 2, 3, 0, 0, 2, 1, 1, 3,
            2, 2, 4, 0, 2, 1, 2, 5, 3, 0, 2, 1, 2, 6, 2, 2, 0, 1, 1, 3, 4, 0, 0, 2, 0, 5, 0, 2, 1,
            0, 2, 2, 2, 2, 1, 3, 0, 1, 4, 2, 1, 1, 1, 0, 0, 2, 0, 1, 0, 1, 3, 2, 2, 2, 1, 2, 3, 1,
            3, 1, 2, 0, 1, 0, 0, 2, 0, 3, 1, 2, 4, 1, 1, 1, 1, 2, 0, 2, 3, 2, 1, 7, 1, 4, 3, 5, 1,
            1, 3, 1, 1, 1, 0, 2, 3, 2, 4, 1, 1, 2, 1, 2, 2, 1, 2, 2, 1, 4, 2, 3, 2, 2, 4, 2, 4, 2,
            3, 1, 1, 1, 2, 0, 1, 2, 1, 1, 2, 2, 1, 3, 1, 1, 2, 1, 1, 2, 2, 3, 2, 1, 0, 0, 1, 0, 3,
            3, 3, 0, 0, 1, 1, 0, 1, 1, 2, 0, 2, 4, 1, 3, 1, 2, 0, 4, 0, 2, 2, 1, 2, 0, 2, 1, 3, 1,
            3, 0, 2, 1, 0, 1, 3, 2, 1, 0, 3, 0, 1, 1, 0, 5, 3, 3, 1, 4, 1, 5, 2, 2, 2, 3, 1, 4, 3,
            3, 2, 3, 2, 4, 3, 3, 1, 0, 2, 0, 3, 3, 1, 2, 1, 2, 0, 1, 2, 0, 2, 2, 1, 1, 2, 0, 0, 1,
            2, 3, 1, 4, 2, 2, 1, 1, 3, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 4, 2, 0,
            0, 3, 0, 0, 1, 1, 0, 1, 2, 1, 3, 2, 2, 4, 1, 3, 3, 2, 1, 2, 1, 3, 2, 2, 3, 3, 0, 2, 3,
            1, 1, 0, 0, 3, 0, 2, 0, 1, 1, 2, 1, 2, 1, 1, 2, 1, 3, 2, 4, 2, 0, 2, 1, 0, 2, 1, 0, 0,
            1, 3, 1, 2, 2, 0, 2, 1, 1, 0, 4, 1, 0, 0, 1, 1, 1, 1, 4, 1, 1, 1, 2, 2, 2, 0, 3, 2, 1,
            2, 1, 3, 2, 2, 0, 1, 1, 1, 4, 1, 1, 2, 1, 1, 1, 2, 1, 0, 1, 0, 1, 0, 1, 3, 0, 3, 1, 2,
            0, 2, 1, 1, 1, 3, 1, 3, 1, 0, 0, 5, 0, 2, 4, 2, 2, 3, 2, 1, 1, 1, 2, 0, 3, 2, 1, 1, 2,
            2, 0, 2, 1, 0, 0, 3, 0, 1, 2, 3, 0, 3, 2, 2, 0, 4, 0, 0, 1, 4, 0, 0, 1, 0, 1, 1, 1, 3,
            1, 1, 1, 0, 4, 1, 2, 0, 0, 1, 2, 1, 0, 1, 0, 1, 2, 1, 0, 1, 1, 2, 2, 2, 0, 0, 0, 2, 0,
            1, 1, 3, 3, 0, 1, 2, 1, 3, 0, 1, 1, 2, 2, 1, 1, 2, 2, 3, 2, 2, 2, 0, 2, 1, 1, 3, 2, 2,
            2, 2, 2, 3, 1, 0, 1, 0, 2, 0, 1, 1, 0, 1, 0, 2, 2, 2, 1, 5, 1, 0, 1, 3, 2, 1, 0, 1, 1,
            3, 2, 1, 2, 1, 2, 0, 2, 1, 1, 1, 0, 0, 0, 1, 1, 1, 4, 0, 0, 1, 1, 1, 0, 1, 0, 2, 3, 0,
            0, 1, 0, 1, 2, 1, 2, 0, 0, 2, 0, 1, 0, 2, 0, 1, 0, 0, 0, 3, 2, 3, 1, 3, 2, 1, 0, 2, 1,
            3, 2, 1, 2, 0, 2, 1, 0, 0, 1, 1, 0, 1, 3, 1, 2, 1, 0, 1, 1, 1, 2, 2, 1, 1, 1, 1, 0, 1,
            3, 0, 2, 0, 1, 2, 3, 1, 0, 2, 1, 1, 3, 1, 2, 1, 3, 1, 3, 0, 1, 2, 0, 0, 0, 1, 3, 0, 0,
            1, 0, 1, 1, 2, 0, 1, 1, 1, 2, 2, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 0, 0, 0, 0, 3, 2, 2, 4,
            2, 2, 4, 0, 0, 0, 0, 0, 0, 2, 2, 3, 2, 0, 0, 1, 0, 1, 1, 2, 2, 2, 0, 0, 0, 1, 3, 3, 1,
            2, 3, 1, 0, 1, 0, 0, 1, 0, 0, 2, 0, 2, 1, 1, 0, 2, 1, 3, 3, 1, 1, 0, 2, 3, 1, 1, 1, 1,
            0, 0, 3, 2, 0, 0, 2, 1, 1, 3, 1, 0, 0, 0, 0, 2, 0, 2, 1, 0, 2, 0, 1, 3, 1, 3, 0, 1, 0,
            0, 1, 1, 0, 1, 2, 0, 2, 0, 0, 1, 0, 3, 2, 3, 2, 0, 0, 2, 1, 1, 3, 0, 1, 4, 3, 4, 2, 0,
            0, 0, 2, 3, 4, 4, 1, 0, 2, 0, 0, 3, 0, 1, 1, 1, 0, 2, 1, 3, 1, 0, 1, 1, 3, 0, 0, 1, 1,
            1, 1, 2, 3, 3, 3, 1, 3, 0, 1, 1, 1, 1, 3, 1, 2, 0, 2, 2, 0, 2, 1, 0, 0, 0, 1, 2, 2, 1,
            1, 1, 0, 2, 0, 4, 2, 3, 0, 0, 2, 0, 1, 3, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 0, 1, 0,
            0, 0, 0, 1, 1, 1, 1, 1, 1, 3, 0, 1, 2, 0, 2, 0, 1, 1, 0, 1, 2, 0, 0, 2, 1, 2, 1, 2, 0,
            1, 0, 1, 3, 3, 0, 1, 1, 1, 0, 1, 1, 2, 0, 3, 2, 1, 0, 1, 1, 0, 0, 2, 3, 0, 0, 0, 2, 5,
            0, 2, 1, 0, 0, 0, 3, 1, 1, 2, 2, 1, 1, 2, 0, 0, 1, 3, 2, 1, 0, 0, 0, 1, 3, 1, 1, 1, 0,
            1, 1, 1, 2, 1, 1, 1, 0, 3, 1, 2, 0, 1, 2, 0, 1, 0, 0, 4, 0, 1, 2, 1, 1, 0, 1, 3, 5, 3,
            0, 3, 1, 0, 2, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 2, 4, 0, 2, 2, 1, 1, 0, 2, 1, 2, 2, 2,
            1, 3, 3, 1, 1, 2, 0, 2, 1, 2, 3, 2, 0, 2, 2, 1, 2, 1, 1, 1, 2, 0, 1, 0, 1, 0, 1, 0, 0,
            2, 2, 3, 0, 2, 3, 4, 1, 3, 0, 1, 0, 1, 0, 1, 1, 1, 0, 2, 2, 1, 2, 0, 1, 1, 2, 2, 1, 3,
            2, 3, 1, 2, 1, 1, 1, 0, 2, 2, 1, 3, 1, 4, 0, 0, 2, 2, 1, 2, 0, 1, 1, 0, 2, 0, 0, 2, 3,
            0, 3, 1, 0, 1, 0, 3, 1, 0, 1, 2, 1, 0, 2, 1, 0, 0, 0, 0, 1, 2, 1, 0, 0, 2, 2, 1, 1, 0,
            0, 2, 2, 2, 1, 1, 3, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 2, 3, 2, 1, 1, 1, 3, 2, 1, 1, 1,
            1, 2, 2, 0, 1, 0, 1, 2, 0, 2, 1, 0, 1, 0, 0, 3, 2, 1, 1, 1, 0, 2, 0, 2, 0, 1, 1, 1, 0,
            1, 1, 2, 0, 0, 0, 4, 0, 2, 4, 2, 1, 0, 1, 0, 1, 0, 1, 3, 1, 2, 1, 2, 1, 3, 0, 0, 3, 1,
            0, 3, 2, 1, 0, 3, 1, 0, 0, 0, 3, 0, 0, 0, 0, 5, 1, 2, 2, 2, 0, 2, 0, 1, 3, 0, 3, 1, 0,
            2, 3, 0, 5, 1, 0, 1, 1, 2, 1, 0, 2, 1, 0, 1, 2, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 2, 0,
            2, 1, 0, 1, 1, 2, 2, 0, 2, 0, 2, 1, 3, 0, 1, 2, 0, 0, 1, 1, 0, 0, 2, 2, 3, 0, 1, 1, 2,
            2, 0, 1, 1, 1, 2, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 2, 0, 0, 1, 0, 1, 1, 0, 1, 0,
            1, 0, 0, 0, 1, 3, 0, 0, 3, 1, 1, 0, 0, 2, 2, 0, 2, 2, 0, 2, 0, 2, 2, 1, 1, 1, 2, 1, 3,
            0, 1, 0, 3, 2, 0, 2, 2, 1, 0, 0, 1, 1, 2, 0, 2, 2, 1, 1, 2, 0, 2, 1, 0, 0, 1, 0, 1, 2,
            1, 2, 1, 1, 0, 1, 3, 0, 2, 0, 2, 3, 0, 1, 0, 1, 1, 1, 2, 0, 2, 1, 0, 1, 1, 3, 0, 3, 0,
            2, 2, 1, 1, 1, 0, 2, 0, 0, 3, 1, 1, 0, 2, 0, 3, 1, 1, 0, 0, 0, 1, 1, 0, 2, 0, 2, 2, 0,
            0, 0, 2, 3, 0, 3, 0, 1, 1, 1, 0, 0, 0, 1, 2, 4, 2, 3, 2, 0, 1, 0, 1, 4, 0, 0, 1, 1, 1,
            2, 0, 1, 1, 2, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 2, 3, 0, 0,
            1, 2, 4, 1, 0, 1, 0, 2, 1, 1, 0, 1, 0, 1, 3, 1, 0, 0, 0, 1, 1, 1, 0, 1, 2, 4, 4, 5, 1,
            0, 0, 2, 2, 0, 3, 0, 1, 1, 2, 1, 0, 0, 2, 0, 2, 0, 0, 1, 5, 0, 1, 0, 0, 1, 0, 0, 2, 1,
            1, 0, 1, 1, 2, 1, 1, 1, 1, 2, 0, 1, 0, 1, 3, 1, 0, 0, 1, 1, 0, 2, 0, 0, 1, 1, 1, 1, 0,
            1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 2, 2, 1, 1, 3, 1, 1, 0, 2, 0, 2, 1, 1, 2, 2, 0, 0, 0, 0,
            1, 0, 1, 1, 3, 1, 3, 1, 0, 2, 1, 1, 4, 0, 1, 4, 1, 0, 1, 3, 2, 1, 0, 0, 1, 1, 1, 0, 1,
            1, 2, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]