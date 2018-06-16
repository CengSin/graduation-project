package com.jingongmn.dao.impl;

import com.jingongmn.dao.ImageSegDao;
import org.omg.SendingContext.RunTime;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Repository;

import java.io.*;

@Repository
public class ImageSegDaoImpl implements ImageSegDao{

    @Value("${PICTURE_PATH}")
    private String PICTURE_PATH;

    private static final String PNG = ".png";

    @Override
    public String getResultImage(String uuid, String segSign) {
        int code = 0;

        Runtime runtime = Runtime.getRuntime();
        String command = "python imgSegmentation1.py "+PICTURE_PATH+uuid+" "+segSign+" "+uuid+PNG;
        try {
            Process exec = runtime.exec(command);
            code = exec.waitFor();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        return code + "";

    }

}
