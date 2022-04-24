import cv2

windowtitle1 = 'fixed'
fixedfp = 'cute.jpg'
readimage1 = cv2.imread(fixedfp, 1)

windowtitle2 = 'Input'
upfp = input("Enter a file path: ")
upff = int(input("Enter a flag (1/0/-1): "))
readimage2 = cv2.imread(upfp, upff)

cv2.imshow(windowtitle1, readimage1)
cv2.imshow(windowtitle2, readimage2)
cv2.waitKey(0)
cv2.destroyAllWindows()