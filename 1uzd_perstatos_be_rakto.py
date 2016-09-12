#!/usr/bin/python
# -*- coding: utf-8 -*-

import itertools
import sys

cypher = """UČKIIAIAPASRNKLISILMRLAIOAASRTIKEVDBSTBIABNAVYPGDUOIĖDUBSMOSIEEUAREEIITONRKKLVDOUSRSRAIUVYKTSDSKILEAUUUOUAAKIAJNSUKNEEUINREIOKŠĖEŽLVJYKĖUSNOTOJIAAIEŲV"""
cypher = cypher.decode('UTF8')

minColumns = int(sys.argv[1])
maxColumns = int(sys.argv[2])

for columnNumber in range(minColumns, maxColumns + 1):
	columnsList = range(0, columnNumber)
	for combination in list(itertools.permutations(columnsList)):
		text = [""] * len(cypher)
		currentCombinationIndex = 0;
		rowCount = 1;
		for cIndex in range(0, len(cypher)):
			text[combination[currentCombinationIndex] * rowCount] = cypher[cIndex]
			currentCombinationIndex += 1
			if currentCombinationIndex == columnNumber:
				currentCombinationIndex = 0
				rowCount += 1
		print(str(columnNumber) + " - " + ''.join(text).encode('UTF8'))
			
			
		
