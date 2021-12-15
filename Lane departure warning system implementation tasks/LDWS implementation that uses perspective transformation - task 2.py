import numpy as np
import cv2
import matplotlib.pyplot as plt


# TODO: napisite funkciju koja oznacava 4 tocke na ulaznoj slici i spaja ih pravcima - za provjeru 4 tocke perspektivne transformacije
def plotArea(image, pts):
    for i in range(0,4):
        cv2.circle(image, (pts[i,0],pts[i,1]), radius=5, color=(255,0,0), thickness=-1)

    cv2.line(image, (pts[0, 0], pts[0, 1]), (pts[1, 0], pts[1, 1]), (0,255,0), thickness=2)
    cv2.line(image, (pts[1, 0], pts[1, 1]), (pts[2, 0], pts[2, 1]), (0, 255, 0), thickness=2)
    cv2.line(image, (pts[2, 0], pts[2, 1]), (pts[3, 0], pts[3, 1]), (0, 255, 0), thickness=2)
    cv2.line(image, (pts[3, 0], pts[3, 1]), (pts[0, 0], pts[0, 1]), (0, 255, 0), thickness=2)


# TODO: napisite funkciju za filtriranje po boji u HLS prostoru
# ulaz je slika u boji, funkcija vraca binarnu sliku te maske za bijelu, zutu boju i ukupnu masku
def filterByColor(image):
    imgHLS = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)

    #definiramo granice maske za bijelu boju
    lower_w = np.uint8([0,200,0])
    upper_w = np.uint8([180,255,255])
    white_mask = cv2.inRange(imgHLS,lower_w, upper_w)

    #definiramo granice maske za zutu boju
    lower_y = np.uint8([20,0,100])
    upper_y = np.uint8([30,255,255])
    yellow_mask = cv2.inRange(imgHLS, lower_y, upper_y)

    #Kombinirajte obje maske pomocu odgovarajuce logicke operacije (bitwise)
    maska = cv2.bitwise_or(white_mask, yellow_mask)

    #Filtirajte sliku pomocu dobivene maske koristei odgovarajucu logicku operaciju (bitwise)
    result = cv2.bitwise_and(image, image, mask=maska)

    return result, yellow_mask, white_mask, maska


# TODO: napisite funkcija koja detektira dva maksimuma u sumi binarne slike po "vertikali"
def getTwoPeaks(binary_img):
    #sumiraj binarnu sliku po vertikali
    column_sums = np.sum(binary_img, axis=0)
    column_sums2 = column_sums.copy()

    #pronadi prvi maksimum
    x1 = np.argmax(column_sums)

    #postavi sve oko njega na nekoj udaljenosti na nulu
    x1_1 = x1 - 150
    x1_2 = x1 + 150

    if x1_1 < 0:
        x1_1 = 0
    if x1_2 > len(column_sums):
        x1_2 = len(column_sums)

    column_sums[x1_1:x1_2] = 0

    #pronadi drugi maksimum
    x2 = np.argmax(column_sums)

    if x1 > x2:
        x_left = x2
        x_right = x1
    else:
        x_left = x1
        x_right = x2

    return x_left, x_right, column_sums2


# TODO: prikazite voznu traku u ulaznoj slici; ako vozilo prelazi u drugu traku tada iskljucite prikaz i ispisite upozorenje
def showLane(original_img, x_left, x_right, y1, y2, M_inv):

    if x_left < 350 and x_right > 800:
        src_left = np.array([[x_left, y1],[x_left,y2]], dtype=np.float32)
        src_right = np.array([[x_right, y1],[x_right,y2]], dtype=np.float32)

        dst_left = cv2.perspectiveTransform(np.array([src_left]), M_inv)
        dst_right = cv2.perspectiveTransform(np.array([src_right]), M_inv)

        dst_left = dst_left[0, :, :]
        dst_right = dst_right[0, :, :]

        pts = np.append(dst_left, np.flip(dst_right, axis=0), axis=0)
        pts = pts.reshape((-1,1,2)).astype(np.int32)

        overlay = original_img.copy()
        cv2.fillPoly(overlay, [pts], color=(0,255,100))
        cv2.addWeighted(overlay, 0.35, original_img, 1-0.35, 0, original_img)

    else:
        cv2.putText(original_img, "Upozorenje!", (int(width/2)-140, 150), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 3, cv2.LINE_4)
    return original_img

def putInfoImg(img, text, loc):
    cv2.putText(img,
                text,
                (loc[0], loc[1]),
                cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0, 255, 255),
                2,
                cv2.LINE_4)



# TODO: Otvorite video pomocu cv2.VideoCapture
video = cv2.VideoCapture("video2.mp4")

# TODO: Spremite sirinu i visinu video okvira u varijable width i height
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

# TODO: Otvorite prozore za prikaz video signala i ostale rezultate (neka bude tipa cv2.WINDOW_NORMAL)
cv2.namedWindow("orginalni video", cv2.WINDOW_NORMAL)
cv2.namedWindow("filter po boji", cv2.WINDOW_NORMAL)


# TODO: Definirajte 4 tocke u ulaznoj slici u numpy polju src, 4 tocke u izlaznoj slici u dst numpy polju
# Izracunajte matricu perspektivne transformacije (M) i njen inverz (M^-1)
# Savjet: iskoristite matplotlib kako biste prikazali jedan video okvir i ocitali zeljene tocke
src = np.array([
    [703, 460],
    [580, 460],
    [205, 720],
    [1110, 720]],
    dtype = np.float32)

dst = np.array([
    [960, 0],
    [320, 0],
    [320, 720],
    [960, 720]],
    dtype = np.float32)

M = cv2.getPerspectiveTransform(src, dst)
M_inv = cv2.getPerspectiveTransform(dst, src)

# TODO: ucitajte sliku i pozovite funkciju koja crta 4 tocke na ulaznoj slici i spaja ih pravcima - kako biste bili sigurni u tocke koje se koriste u transfromaciji
# Trebate najprije pohraniti jedan reprezentativni okvir na disk iz danog video signala



time = 1
k = 0
while True:
    e1 = cv2.getTickCount()
    # TODO: Ucitaj video okvir (frame) pomocu metode read, povecaj k za jedan ako je uspjesno ucitan
    ret, frame = video.read()
    if ret == False:
        print("video end")
        break
    else:
        k += 1

    frame_cpy = frame.copy()

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

    # TODO: Pozovite funkciju za filtriranje po boji nad ulaznim okvirom
    frameFiltered, yellow_mask, white_mask, maska = filterByColor(frame)

    # TODO: Transformirajte filtriranu binarnu sliku
    warped_img = cv2.warpPerspective(maska, M, (width, height), flags=cv2.INTER_LINEAR)

    # TODO: Pozovite funkciju koja pronalazi dva maksimuma u "vertikalnoj sumi" transformirane binarne slike
    x_left, x_right, column_sums2 = getTwoPeaks(warped_img)

    # TODO: Pozovite funkciju koja oznacava voznu traku u originalnom video okviru; u slucaju prelaska u drugu ispisuje upozorenje 
    frame_final = showLane(frame, x_left, x_right, 0, maska.shape[0], M_inv)

    # TODO: Izracunajte vrijeme obrade u fps
    e2 = cv2.getTickCount()
    time = (e2 - e1)/cv2.getTickFrequency()

    # TODO: Prikazite vrijeme obrade i redni broj okvira u gornjem lijevom cosku ulaznog video okvira
    putInfoImg(frame, "frame: " + str(k), ((50,50)))
    putInfoImg(frame, "FPS: " + str(int(1/time)), ((50,100)))

    # TODO: Prikazite okvir pomocu cv2.imshow(); i sve ostale medjurezultate kada ih napravite
    cv2.imshow("orginalni video", frame)
    cv2.imshow("filter po boji", frameFiltered)
    cv2.imshow("warped image", warped_img)
    cv2.imshow("result", frame_final)

    # plt.figure()
    # plt.plot(np.linspace(0,len(columns_sums2), len(columns_sums2)), columns_sums2)
    # plt.show()


    # TODO: Ispisite vrijeme procesiranja jednog okvira
    print("Vrijeme obrade u fps: ", 1.0 / time)

# TODO: Unistite sve prozore i oslobodite objekt koji je kreiran pomocu cv2.VideoCapture
video.release()
cv2.destroyAllWindows()