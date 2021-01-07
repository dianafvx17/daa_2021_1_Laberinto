{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "ADT.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPy0XqkEwM+8zF1LSBj5lcd",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/dianafvx17/daa_2021_1_Laberinto/blob/main/ADT.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_-zC_wpUG9aZ"
      },
      "source": [
        "desde  arreglos  importar  Array2D\r\n",
        "de  pilas  import  Stack\r\n",
        "\r\n",
        "class  ADT :\r\n",
        "    def  __init__ ( self , archivo_inicio ):\r\n",
        "        archivo  =  open(archivo_inicio,'rt')\r\n",
        "        self.__laberinto  =  Array2D( int ( archivo.readline().strip()), int ( archivo.readline().strip()), '1' )\r\n",
        "        self.__laberinto.clearing( '1' ) # todo pared\r\n",
        "        self.__entrada = []\r\n",
        "        self.__salida = []\r\n",
        "        self.__camino  =  Pila()\r\n",
        "        self.__previa  =  Ninguno\r\n",
        "\r\n",
        "        lineas  =  archivo.readlines()\r\n",
        "        for  ren  in range(len(lineas)):\r\n",
        "            lineas[ren] = lineas[ren].tira()\r\n",
        "            col = 0\r\n",
        "            for  celda  in  lineas[ren].dividir( ',' ):\r\n",
        "                self.__laberinto.set_item(ren,col,celda)\r\n",
        "                col  + =  1\r\n",
        "    def  set_previa ( self , posicion ):\r\n",
        "        self.__previa = posicion\r\n",
        "\r\n",
        "    def  get_previa (self):\r\n",
        "        return self.__previa\r\n",
        "\r\n",
        "    def  mostrar_laberinto ( self ):\r\n",
        "        #self .__ laberinto.to_string ()\r\n",
        "        for  row  in range(self.__laberinto.get_num_rows()):\r\n",
        "            for  col  in range(self.__laberinto.get_num_cols()):\r\n",
        "                #print (self.string_to_wall (self .__ laberinto.get_item (ren, col)), end = '')\r\n",
        "                self.string_to_wall(self.__laberinto.get_item( row , col ))\r\n",
        "            print( \"\" )\r\n",
        "\r\n",
        "    def  mostrar_actual ( self ):\r\n",
        "        lab  =  self.__laberinto\r\n",
        "        actual  =  self.__camino.mirar ()\r\n",
        "        laboratorio.set_item( real[0], real[1], 'A' )\r\n",
        "\r\n",
        "        for  ren  in range(lab.get_num_rows()):\r\n",
        "            for  col in range(lab.get_num_cols()):\r\n",
        "                self.string_to_wall(lab.get_item( ren , col ))\r\n",
        "\r\n",
        "            print( \"\" )\r\n",
        "\r\n",
        "\r\n",
        "    def  string_to_wall ( self , celda ):\r\n",
        "        if  celda  ==  '1' :\r\n",
        "            print(\r\n",
        "                    \"{} {} {}\" .formato (\r\n",
        "                        bg ( 'blanco' ),\r\n",
        "                        '' ,\r\n",
        "                        attr ( \"reiniciar\" )), end = '' )\r\n",
        "        elif  celda ==  '0' :\r\n",
        "            print(\r\n",
        "                    \"{} {} {}\" .formato (\r\n",
        "                        bg ( 'negro' ),\r\n",
        "                        '' ,\r\n",
        "                        attr ( \"reiniciar\" )), end = '' )\r\n",
        "        elif  celda  ==  'E' :\r\n",
        "            print(\r\n",
        "                    \"{} {} {}\" .formato (\r\n",
        "                        bg ( 'azul' ),\r\n",
        "                        'E' ,\r\n",
        "                        attr ( \"reiniciar\" )), end = '' )\r\n",
        "        elif  celda  ==  'S' :\r\n",
        "            print(\r\n",
        "                    \"{} {} {}\" .formato (\r\n",
        "                        bg ( 'verde' ),\r\n",
        "                        'S' ,\r\n",
        "                        attr ( \"reiniciar\" )), end = '' )\r\n",
        "        elif  celda  ==  'C' :\r\n",
        "            print(\r\n",
        "                    \"{} {} {}\" .formato (\r\n",
        "                        bg ( 'verde_claro' ),\r\n",
        "                        '' ,\r\n",
        "                        attr ( \"reiniciar\" )), end = '' )\r\n",
        "        elif  celda  ==  'A' :\r\n",
        "            print(\r\n",
        "                    \"{} {} {}\" .formato (\r\n",
        "                        bg ( 'verde_claro' ),\r\n",
        "                        '' ,\r\n",
        "                        attr ( \"reiniciar\" )), end = '' )\r\n",
        "        else:\r\n",
        "            print(\r\n",
        "                    \"{} {} {}\" .formato (\r\n",
        "                        bg ( 'rojo' ),\r\n",
        "                        '' ,\r\n",
        "                        attr ( \"reiniciar\" )), end = '' )\r\n",
        "\r\n",
        "    def  set_entrada ( self ):\r\n",
        "        encontrada  =  Falso\r\n",
        "        for  ren  in range( self.__laberinto.get_num_rows()):\r\n",
        "            for  col  in range( self.__laberinto.get_num_cols()):\r\n",
        "                if  self.__laberinto.get_item( ren , col ) ==  'E' :\r\n",
        "                    self.__entrada = [ ren , col ]\r\n",
        "                    encontrada  =  Verdadero\r\n",
        "                    self.__camino.empujar ([ ren , col ])\r\n",
        "        return  encontrada\r\n",
        "\r\n",
        "    def  set_salida ( yo ):\r\n",
        "        encontrada  =  Falso\r\n",
        "        for  ren  in range( self.__laberinto.get_num_rows()):\r\n",
        "            for  col  in range( self.__laberinto.get_num_cols()):\r\n",
        "                if  self.__laberinto.get_item( ren , col ) ==  'S' :\r\n",
        "                    self.__salida = [ ren , col ]\r\n",
        "                    encontrada  =  Verdadero\r\n",
        "        return  encontrada\r\n",
        "\r\n",
        "    def  agragar_solucion ( self ):\r\n",
        "        while not is self.__camino.is_empty ():\r\n",
        "            paso = self.__camino.pop()\r\n",
        "            self.__laberinto.set_item ( paso [ 0 ], paso [ 1 ], 'C' )\r\n",
        "\r\n",
        "\r\n",
        "    def  resolver ( auto ):\r\n",
        "        actual  =  self.__camino.mirar()\r\n",
        "\r\n",
        "        # revisar izq\r\n",
        "        if  self.__laberinto.get_item( real [ 0 ], real [ 1 ] - 1 ) ==  '0' \\\r\n",
        "            and  self.__laberinto.get_item( actual [ 0 ], actual [ 1 ] - 1 ) ! =  'X' \\\r\n",
        "            and self.get_previa() ! = [ actual [ 0 ], actual [ 1 ] - 1 ]:\r\n",
        "            #print ('mover izq')\r\n",
        "            self.set_previa ( actual )\r\n",
        "            self.__camino.empujar([ actual [ 0 ], actual [ 1 ] - 1 ])\r\n",
        "        # revisar arriba\r\n",
        "        elif  self.__laberinto.get_item( real [ 0 ] - 1 , real [ 1 ]) ==  '0'   \\\r\n",
        "        and  self.__laberinto.get_item( actual [ 0 ] - 1 , actual [ 1 ]) ! =  'X' \\\r\n",
        "        and  self.get_previa() ! = [ actual [ 0 ] - 1 , real [ 1 ]]:\r\n",
        "            #print ('mover arriba')\r\n",
        "            self.set_previa( actual )\r\n",
        "            self.__camino.empujar([ actual [ 0 ] - 1 , actual [ 1 ]])\r\n",
        "        # revisar der\r\n",
        "        elif  self.__laberinto.get_item( real [ 0 ], real [ 1 ] + 1 ) ==  '0' \\\r\n",
        "        and  self.__laberinto.get_item( actual [ 0 ], actual [ 1 ] + 1 ) ! =  'X' \\\r\n",
        "        and  self.get_previa() ! = [ actual [ 0 ], actual [ 1 ] + 1 ]:\r\n",
        "            #print ('mover derecha')\r\n",
        "            self.set_previa( actual )\r\n",
        "            self.__camino.empujar([ actual [ 0 ], actual [ 1 ] + 1 ])\r\n",
        "        # revisar abajo\r\n",
        "        elif  self.__laberinto.get_item( real [ 0 ] + 1 , real [ 1 ]) ==  '0' \\\r\n",
        "        and self.__laberinto.get_item( real [ 0 ] + 1 , real [ 1 ]) ! =  'X' \\\r\n",
        "        and self.get_previa() ! = [ actual [ 0 ] + 1 , real [ 1 ]]:\r\n",
        "            #print ('mover abajo')\r\n",
        "            self.set_previa( actual )\r\n",
        "            self.__camino.empujar([ actual [ 0 ] + 1 , actual [ 1 ]])\r\n",
        "        else:\r\n",
        "            self.__laberinto.set_item( real [ 0 ], real [ 1 ], 'X' )\r\n",
        "            self.__camino.pop()\r\n",
        "\r\n",
        "\r\n",
        "    def  imprime_camino(self):\r\n",
        "        self.__camino.to_string()\r\n",
        "\r\n",
        "    def  es_la_salida ( self ):\r\n",
        "        actual  =  self.__camino.mirar()\r\n",
        "        test:\r\n",
        "            if  self.__laberinto.get_item( real [ 0 ], real [ 1 ] - 1 ) == 'S' :\r\n",
        "                return True\r\n",
        "            elif  self.__laberinto.get_item( real [ 0 ] - 1 , real [ 1 ]) == 'S' :\r\n",
        "                return True\r\n",
        "            elif  self.__laberinto.get_item( real [ 0 ], real [ 1 ] + 1 ) == 'S' :\r\n",
        "                return True\r\n",
        "            elif  self.__laberinto.get_item( real [ 0 ] + 1 , real [ 1 ]) == 'S' :\r\n",
        "                return True\r\n",
        "            else:\r\n",
        "                return False\r\n",
        "\r\n",
        "        except e :\r\n",
        "            print( f \"Error: { e } \" )\r\n",
        "\r\n",
        "\r\n",
        "\r\n",
        "def  main ():\r\n",
        "\r\n",
        "    laberinto  =  ADT ( './entrada.lab' )\r\n",
        "    laberinto.mostrar_laberinto ()\r\n",
        "    if  laberinto.set_entrada ():\r\n",
        "        while not self.es_la_salida():\r\n",
        "            laberinto.resolver ()\r\n",
        "            #system ('borrar')\r\n",
        "            laberinto.mostrar_actual()\r\n",
        "            tiempo.dormir( 0.08 )\r\n",
        "        laberinto.imprime_camino ()\r\n",
        "        laberinto.agragar_solucion () #vacia la pilas\r\n",
        "        laberinto.mostrar_laberinto ()\r\n",
        "    else:\r\n",
        "        print( \"No hay entrada\" )\r\n",
        "main()"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}