import { useEffect, useState } from "react";
import "./App.css";
import Loader from "./components/loader/Loader";
import imageService from "./services/image.service";

function App() {
  const [imageList, setImageList] = useState([]);
  const [brightness, setBrightness] = useState<number>(10);
  const [contrast, setContrast] = useState<number>(10);
  const [loading, setLoading] = useState<boolean>(true);
  const [imageId, setImageId] = useState<number | undefined>();
  const [selectedOriginalImage, setSelectedOriginalImage] =
    useState<string>("");
  const [selectedProcessedImage, setSelectedProcessedImage] =
    useState<string>("");

  const fetchImageList = async () => {
    setLoading(true);
    await imageService
      .getImages()
      .then((response) => {
        setImageList(response);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Erro ao obter lista de imagens:", error);
      });
  };

  const fetchAPI = async () => {
    await imageService
      .testAPI()
      .then((response) => {
        if (response == "OK") {
          fetchImageList();
        } else {
          setTimeout(fetchAPI, 1000);
        }
      })
      .catch((error) => {
        console.error("Erro ao obter a imagem:", error);
      });
  };

  useEffect(() => {
    const intervalId = setTimeout(fetchAPI, 1000);
    return () => clearInterval(intervalId);
  }, []);

  const sendImage = async (event: any) => {
    event.preventDefault();
    const file = event.target.files[0];
    const formData = new FormData();
    formData.append("file", file);
    await imageService
      .uploadImage(formData)
      .then((response) => {
        setImageList(response);
      })
      .catch((error) => {
        console.error("Erro ao enviar a imagem:", error);
      });
  };

  const getImage = async (id: number) => {
    setImageId(id);
    await imageService
      .getOriginalImage(id)
      .then((response) => {
        const imageUrl = URL.createObjectURL(response);
        setSelectedOriginalImage(imageUrl);
      })
      .catch((error) => {
        console.error("Erro ao obter a imagem original:", error);
      });
    await imageService
      .getProcessedImage(id)
      .then((response) => {
        const imageUrl = URL.createObjectURL(response);
        setSelectedProcessedImage(imageUrl);
      })
      .catch((error) => {
        console.error("Erro ao obter a imagem processada:", error);
      });
  };

  const getImageList = () => {
    return imageList.map((item: { id: number; image: string }) => {
      return (
        <button
          className="select-image-button unselectable"
          key={item.id}
          onClick={() => getImage(item.id)}
        >
          {item.image}
        </button>
      );
    });
  };

  const operation = async (operationName: string, operationValue: number) => {
    await imageService
      .processesImage(imageId, operationName, operationValue)
      .then((response) => {
        const imageUrl = URL.createObjectURL(response);
        setSelectedProcessedImage(imageUrl);
      })
      .catch((error) => {
        console.error("Erro ao processar imagem:", error);
      });
  };

  return (
    <div className="">
      {loading ? (
        <Loader />
      ) : (
        <>
          <input
            className="upload-file-input"
            type="file"
            onChange={sendImage}
          />
          <div className="main-row">
            <div className="image-list">
              <h3>Images</h3>
              {getImageList()}
            </div>
            <div className="original-image-wrapper">
              {selectedOriginalImage && (
                <>
                  <p>Original</p>
                  <img src={selectedOriginalImage} className="image-shower" />
                </>
              )}
            </div>
            <div className="processed-image-wrapper">
              {selectedProcessedImage && (
                <>
                  <p>Processed</p>
                  <img src={selectedProcessedImage} className="image-shower" />
                </>
              )}
            </div>
            <div className="operation-list-wrapper">
              <h3>Operatiosn</h3>
              <button
                className="select-image-button unselectable"
                onClick={() => operation("rotate", 90)}
              >
                rotate 90°
              </button>
              <button
                onClick={() => operation("rotate", 180)}
                className="select-image-button unselectable"
              >
                rotate 180°
              </button>
              <button
                onClick={() => operation("flip", 0)}
                className="select-image-button unselectable"
              >
                Flip Horizontal
              </button>
              <button
                onClick={() => operation("flip", 1)}
                className="select-image-button unselectable"
              >
                Flip Vertical
              </button>
              <p>Contrast: {contrast / 10}</p>
              <input
                type="range"
                defaultValue="10"
                min="0"
                max="50"
                onChange={(event: any) => setContrast(event.target.value)}
                onMouseUp={(event: any) =>
                  operation("contrast", event.target.value / 10)
                }
              />
              <p>Brightness {brightness / 10}</p>
              <input
                type="range"
                defaultValue="10"
                min="0"
                max="20"
                onChange={(event: any) => setBrightness(event.target.value)}
                onMouseUp={(event: any) =>
                  operation("brightness", event.target.value / 10)
                }
              />
            </div>
          </div>
        </>
      )}
    </div>
  );
}

export default App;
