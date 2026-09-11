#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script para detectar caracteres bidireccionales problemáticos en archivo
"""

import re

# Caracteres bidireccionales peligrosos
PROBLEMATICOS = {
    '\u202A': 'LEFT-TO-RIGHT EMBEDDING (U+202A)',
    '\u202B': 'RIGHT-TO-LEFT EMBEDDING (U+202B)',
    '\u202C': 'POP DIRECTIONAL FORMATTING (U+202C)',
    '\u202D': 'LEFT-TO-RIGHT OVERRIDE (U+202D)',
    '\u202E': 'RIGHT-TO-LEFT OVERRIDE (U+202E)',
    '\u2066': 'LEFT-TO-RIGHT ISOLATE (U+2066)',
    '\u2067': 'RIGHT-TO-LEFT ISOLATE (U+2067)',
    '\u2068': 'FIRST STRONG ISOLATE (U+2068)',
    '\u2069': 'POP DIRECTIONAL ISOLATE (U+2069)',
    '\u061C': 'ARABIC LETTER MARK (U+061C)',
    '\u200E': 'RIGHT-TO-LEFT MARK (U+200E)',
    '\u200F': 'LEFT-TO-RIGHT MARK (U+200F)',
    '\u200B': 'ZERO WIDTH SPACE (U+200B)',
    '\u200C': 'ZERO WIDTH NON-JOINER (U+200C)',
    '\u200D': 'ZERO WIDTH JOINER (U+200D)',
    '\uFEFF': 'ZERO WIDTH NO-BREAK SPACE (U+FEFF)',
}

def detectar_caracteres(nombre_archivo):
    """Detecta caracteres problemáticos en el archivo"""
    
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as f:
            lineas = f.readlines()
    except Exception as e:
        print(f"❌ Error al leer archivo: {e}")
        return
    
    encontrados = []
    
    for num_linea, linea in enumerate(lineas, 1):
        for pos, char in enumerate(linea):
            if char in PROBLEMATICOS:
                encontrados.append({
                    'linea': num_linea,
                    'posicion': pos,
                    'caracter': PROBLEMATICOS[char],
                    'contenido': linea.strip()
                })
    
    if not encontrados:
        print(f"✅ ¡BIEN! No se encontraron caracteres bidireccionales en '{nombre_archivo}'")
        return
    
    print(f"⚠️  Se encontraron {len(encontrados)} caracteres problemáticos:\n")
    print("=" * 100)
    
    for item in encontrados:
        print(f"\n📍 LÍNEA {item['linea']}, POSICIÓN {item['posicion']}")
        print(f"   Tipo: {item['caracter']}")
        print(f"   Contenido: {item['contenido'][:80]}...")
        print("-" * 100)
    
    print(f"\n✅ Reporte completado. Total: {len(encontrados)} caracteres encontrados")

if __name__ == '__main__':
    detectar_caracteres('Latino')
