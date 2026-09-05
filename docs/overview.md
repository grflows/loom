## introduction
Loom is basically a statically-typed lua-like skin for js. As such it is transpiled to standard js code.
Loom aims to be simple, that's it.

## the basics

### hello world
just print it. The syntax is lua-like.

``` js
print "Hello world"
```

### vars
Loom is statically-typed.
declare a var just like in any other lang.

``` c
int number
str name = "foo"
err error
```

### control flow
same as lua
``` lua
if condition
  // do
else
  // do something else
end
```

### comments 

// this is a comment


## new features
some features to make js a bit more fun 

### objects mapping
to js, everything is an object, even DOM elements. So I made mapping easier.

instead of:
```js

const playbtn = document.getElementById('play');
```

loom uses:
``` lua  

map playbtn to objWithId('play')
```

you can even batch map them:
``` c

map
  playbtn objWithId('play')
  prevbtn objWithId('previous')
  nextbtn objWithId('next')
end
  ```

you get the idea.

### eval keyword and type checking
use the eval keyword to evaluate a statement get the result, optionally pass it through a type checker using ?, or pipe it directly where you want.

For example:

``` c
int bar
eval foo() + 99
| bar // pipe foo's output to bar

// or if you want to typecheck it
eval foo() + 99
? int >> bar
? err >> handle_err(err) // err is both a type and an var

// another example
eval r of fetch(url) // use an intermediate var when passing to a function
? json >> parseApiResponse(r)
? err  >> handle_err(err)

// another one 
eval r,x of db.getUser(userID)
? str, int >> loadUserDate(r, x)
? err      >> data_base_fallback(err)
```


### debugging annotations
basically a fancy print for various cases

```c 
int x
x = randInt(100) ?var // prints x's current value

eval foo(bar) ?val // prints foo's return
? int >> x

int y ?mut // prints every y mutation

foo(bar1, bar2, bar3) ?val // prints the function's current args 

func foo(int bar) -> void ?call // prints every call to foo()
  // something
end

foo(bar) ?trace // traces the last function call

int secret = 1149193843 ?read // prints every time secret is accessed

someWeirdfunc(arg1, arg2, arg3) ?type // prints the types expected and types returned

_ = someWeirdvar ?type // prints the type of the var
// also _ is meant as a temp typeless var


```

### raw js 
for when you want to write js directly
```c 

raw
  // your js code, can use all vars and funcs in loom
end
```


