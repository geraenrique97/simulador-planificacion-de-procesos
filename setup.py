#!/usr/bin/python
# -*- coding: utf-8 -*-
 
from cx_Freeze import setup, Executable
 
setup(
 name="Simulador",
 version="1.0",
 author='Enrique Gerardo, Federico Zimmermann',
 description="Simulador de un planificador de procesos. Realizado para la materia: Sistemas Operativos. UTN FRRe",
 executables = [Executable("simulador.py")],
 )