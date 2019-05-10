# JupyterNoteboob and JupyText

Dentro de los metadatos del jupyter notebook, hemos añadido las siguientes lineas: 

```json
{
  "jupytext": {"formats": "ipynb,py"},
  "kernelspec": {
    (...)
  },
  "language_info": {
    (...)
  }
}
```

De esta forma, al cargar desde Jupyter el ipynb, los datos serán leidos del archivo .py

Para más informacion ir al siguiente [enlace](https://nextjournal.com/schmudde/how-to-version-control-jupyter)