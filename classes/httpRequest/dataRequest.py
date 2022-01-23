#!/usr/bin/python3

# On importe les librairies nécessaires
import hmac
import hashlib
import time
import json
import requests
from typing import Any

# On crée la classe de dataRequest
class dataRequest:
	"""
        Classe permettant de faire les requêtes à la base de données

        :author: Delmas Pierre <panda@delmasweb.net>
        :date: 30 Août 2021
        :version: 0.3
    """

	def __init__(self, apiKey : str) -> None:
		"""
			Constructeur

			:param apiKey: La clé de l'API à laquelle on se connecte
			:type apiKey: str
			:rtype: None
		"""
		self.__setApiKey(apiKey)
	
	def __setApiKey(self, apiKey : str) -> None:
		"""
			Mutateur de la clé d'API

			:param apiKey: La clé d'API
			:type apiKey: str
			:rtype: None
			:meta private:
		"""
		self.__apiKey = apiKey
	
	def __getApiKey(self) -> str:
		"""
			Accesseur de la clé d'API

			:returns: La clé d'API
			:rtype: str
			:meta private:
		"""
		return self.__apiKey

	def __makeRequest(self, uri : str, url : str, getParams : str, payload : str, methodHTTP : str) -> Any:
		"""
			Cette méthode fait les appels HTTP REST API

			:param uri: L'URI du site où l'on souhaite faire la requete
			:type uri: str
			:param url: Le chemin d'accès sur le serveur
			:type url: str
			:param getParams: Les paramètres que l'on passe dans l'URL après le ?
			:type getParams: str
			:param payload: Un objet au format JSON serialisé en chaîne de caractère (voir json.dumps)
			:type payload: str
			:param methodHTTP: La méthode HTTP d'appel (i.E GET, POST)
			:type methodHTTP: str
			:raise Exception: Une exception est levée si jamais la réponse à la requete est >=400
			:meta private:
		"""
		url = uri+"/"+url+"?"+getParams+"&appid="+self.__getApiKey()

		headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
		response = None

		if methodHTTP=="GET":
			response = requests.get(url)
		elif methodHTTP=="POST":
			response = requests.post(url, data=payload, headers=headers)

		if response!=None and response.status_code<400:
			return response.json()
		else:
			raise Exception("Request failed with code : "+str(response.status_code)+" and error is "+response.text)
	
	def __createConnectionPayload(self, params : dict) -> str:
		"""
			Cette méthode créé la charge utile pour l'envoi de requête sous le format d'un objet JSON sérialisé

			:param params: Un dictionnaire qui sera transformé au format JSON
			:type params: dict
			:meta private:
		"""
		req = params;

		return json.dumps(req)

	def makeRequest(self, uri : str, url : str, getParams : str="", params : dict={}, methodHTTP : str="GET") -> Any:
		"""
			Cette méthode est la méthode public pour faire les appels à l'API

			:param uri: L'URI de l'API
			:type uri: str
			:param url: La partie qui identifie sur le site désignée par l'URI
			:type url: str
			:param getParams: Optional; Default : ""; Les paramètres a fournir pour les requetes derriere le ?
			:type getParams: str
			:param params: Optional; Default: {}; Le JSON a envoyé
			:type params: dict
			:param methodHTTP: Optional; Default : GET; Défini la méthode d'appel HTTP (i.e GET, POST)
			:type methodHTTP: str
			:returns: Le résultat de la requête au format JSON
			:raise: L'Exception produite en cas d'echec de connexion
			:rtype: Any
			:meta public:
		"""
		try:
			payload = self.__createConnectionPayload(params)
			return self.__makeRequest(uri, url, getParams, payload, methodHTTP)
		except Exception as e :
			raise e
		
	
		
		
