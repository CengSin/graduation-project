package com.jingongmn.controller;

import com.jingongmn.service.ImageSegService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;

@RestController
@RequestMapping("/image")
public class ImageSeg {

    private ImageSegService service;

    @Autowired
    public ImageSeg(ImageSegService service) {
        this.service = service;
    }

    @CrossOrigin
    @GetMapping
    public String getRestultImage(@RequestParam String uuid, @RequestParam String segSign) {
        return service.getResultImage(uuid, segSign);
    }

    @PostMapping
    public void uploadImage(@RequestParam("file") MultipartFile file) {

        byte[] bytes = null;
        try {
            // 通过MultipartFile类对象的getBytes()方法可获得上传文件的内容
            bytes = file.getBytes();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}
