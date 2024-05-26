import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8080/",
});

async function testAPI() {
  const response = await api.get("");
  return response.data;
}

async function uploadImage(image: any) {
  const response = await api({
    method: "post",
    url: "upload",
    data: image,
    headers: { "Content-Type": "multipart/form-data" },
  });
  return response.data;
}

async function getImages() {
  const response = await api({
    method: "get",
    url: "images",
  });
  return response.data;
}

async function getOriginalImage(imageId: number) {
  const response = await api({
    method: "get",
    url: "originalImageFile",
    params: { id: imageId },
    responseType: "blob",
  });
  return response.data;
}

async function getProcessedImage(imageId: number) {
  const response = await api({
    method: "get",
    url: "imageFile",
    params: { id: imageId },
    responseType: "blob",
  });
  return response.data;
}

async function processesImage(
  imageId: number | undefined,
  operation: string,
  value: number
) {
  if (imageId == undefined) return;
  const response = await api({
    method: "put",
    url: "process",
    params: { id: imageId, operation: operation, value: value },
    responseType: "blob",
  });
  return response.data;
}

const imageService = {
  testAPI,
  uploadImage,
  getImages,
  getOriginalImage,
  getProcessedImage,
  processesImage,
};
export default imageService;
