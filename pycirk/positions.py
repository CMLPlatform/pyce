# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 10:58:46 2019

Description: Finding the position of labels

Scope: Modelling the Circular Economy in EEIO

@author:Franco Donati
@institution:Leiden University CML
"""

import numpy as np

# Started doing some generalization work, but still in the process
# I don't know whether it's worth the effort.
# Maybe somebody else will want to give a crack at it


def single_position(item, labels):
    """
    Takes a dataframe of the multiindex and identifies the position
    of the specified values
    """

    if item in ["All", "all", "ALL", np.nan]:
        coordinate = None

    else:
        try:
            if item in labels:
                ref_labels = labels
        except Exception:
            pass

        try:
            if item in labels.name:
                ref_labels = labels.name
            elif item in labels.synonym:
                ref_labels = labels.synonym
            elif item in labels.code:
                ref_labels = labels.code
        except Exception:
            pass

        try:
            if item in labels.characterization:
                ref_labels = labels.characterization
        except Exception:
            pass

        coordinate = np.array([i for i, values in enumerate(ref_labels)
                              if item in values])

    return(coordinate)


def make_coord_array(cat_coord, reg_coord, no_countries, no_categories):

    if no_categories not in [7, 163, 200]:
        no_countries = 1
    else:
        pass

    if cat_coord is None:
        s = np.array(range(no_categories * no_countries))
    else:
        n = 0
        while n in range(no_countries):
            g = cat_coord[0] + no_categories * n
            if "s" not in locals():
                s = g
            else:
                s = np.hstack([s, g])
            n = n+1

    if reg_coord is None:
        pass
    else:
        s = np.split(s, no_countries)
        s = np.take(s, reg_coord, axis=0)[0]

    return(s)
