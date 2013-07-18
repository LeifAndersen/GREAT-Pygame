import pygame

class Resources:
	def convertToAlpha(sourceImage, transparencyColor):
		sourceImage.set_colorkey(transparencyColor)
		return sourceImage

	def spriteSheetToArray(sourceImage, numberRows, numberColumns, transparencyColor):
		imageArray = []
		sourceRect = sourceImage.get_rect()
		spriteWidth = sourceRect.width/numberColumns
		spriteHeight = sourceRect.height/numberRows

		for rows in range(numberRows):
			for cols in range(numberColumns):
				subImage = sourceImage.subsurface(pygame.Rect((spriteWidth*cols,
													spriteHeight*rows),(spriteWidth,spriteHeight)))
				subImage.set_colorkey(transparencyColor)
				imageArray.append(subImage)

		return imageArray