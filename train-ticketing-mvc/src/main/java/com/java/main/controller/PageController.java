package com.java.main.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.ui.ModelMap;
import org.springframework.validation.BindingResult;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import javax.validation.Valid;
import com.java.main.dao.TrainsDao;
import com.java.main.entity.Trains;

@Controller
public class PageController {
	@Autowired
    TrainsDao trainsDao;

    @RequestMapping("/users")
    public String home(Model model) {
         model.addAttribute("users", trainsDao.findAll());
         return "users";
    }
    
    @RequestMapping(value = "/users", method = RequestMethod.POST)
    public String submit(@Valid @ModelAttribute("train")Trains train, 
      BindingResult result, ModelMap model) {
        if (result.hasErrors()) {
            return "error";
        }
        model.addAttribute("source", train.getSource());
        model.addAttribute("destination", train.getDestination());
        model.addAttribute("id", train.getId());
        return "list";
    }
}
