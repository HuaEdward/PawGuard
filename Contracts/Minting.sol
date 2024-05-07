// SPDX-License-Identifier: MIT

pragma solidity ^0.8.2;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract PawNFT is ERC721, Ownable {
    uint256 private _nextTokenId;
    mapping(address => bool) private _hasMinted;
    uint256 private _scoreThreshold = 6500;

    mapping(uint256 => string) private _tokenSpecies;

    constructor(
        address initialOwner
    ) ERC721("PawNFT", "Paw") Ownable(initialOwner) {}

    function _baseURI() internal pure override returns (string memory) {
        return "https://raw.githubusercontent.com/HuaEdward/PawGuard/main/Contracts/url.json";
    }

    function safeMint(address to, uint256 score, string memory species) public onlyOwner {
        require(!_hasMinted[to], "This address has already minted an NFT.");
        require(score > _scoreThreshold, "Score must be greater than 6500.");

        uint256 tokenId = _nextTokenId++;
        _safeMint(to, tokenId);
        _hasMinted[to] = true;

        // Store the species of the token
        _tokenSpecies[tokenId] = species;
    }

    // Get the species of a token
    function getTokenSpecies(uint256 tokenId) public view returns (string memory) {
        return _tokenSpecies[tokenId];
    }
}
