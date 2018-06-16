package com.jingongmn.service.impl;

import com.jingongmn.dao.ImageSegDao;
import com.jingongmn.service.ImageSegService;
import org.springframework.stereotype.Service;

@Service
public class ImageSegServiceImpl implements ImageSegService{

    private ImageSegDao dao;

    public ImageSegServiceImpl(ImageSegDao dao) {
        this.dao = dao;
    }

    @Override
    public String getResultImage(String uuid, String segSign) {
        return dao.getResultImage(uuid, segSign);
    }
}
