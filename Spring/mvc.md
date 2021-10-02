

 ```
 EntityModel<User> model = new EntityModel<>(user);;
 WebMvcLinkBuilder linkTo = linkTo(methodOn(this.getClass()).retieveAllUsers());
 model.add(linkTo.withRel("all-users"));
 
 return model
 ```

