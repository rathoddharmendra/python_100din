Day 61 - points to remember

`
pip freeze >> requirements-test.txt
`

# Include template as fixed template
`{% include 'template' %}`

## Template Inheritance using super()
`{% extends 'template' %}`
* using blocks to overwrite 
  * In base.html `{% block block_name %} {% end block %}`
  * In child.html `{% block block_name %} write content here {% end block %}`
* Super Blocks
  * When we inherit from Python classes, you often see super.init()
  * When we are inheriting templates. Sometimes, there's some part of the template that we want to keep, but we also want to add to it. So we can use super blocks in this case.
  * use: `{{ super() }}` to display or include base block content along with child arguments
    * in base.html `{% block block_name %} super content {% end block %}`
    * in child.html `{% block block_name %} {{ super() }} child additional arguments content {% end block %}`

